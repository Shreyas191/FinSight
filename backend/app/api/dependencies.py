"""
Shared dependencies and model loading
"""

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import chromadb
import torch
import google.generativeai as genai
from app.config import settings
import os

class ModelDependencies:
    """Container for all loaded models"""
    def __init__(self):
        self.embedding_model = None
        self.gemini_model = None
        self.sentiment_analyzer = None
        self.chroma_client = None
        self.collection = None
        self.document_store = {}

# Global model instance
_models = None

def get_models() -> ModelDependencies:
    """Get or initialize models (singleton pattern)"""
    global _models
    
    if _models is None:
        print("Loading models for the first time...")
        _models = ModelDependencies()
        
        # Load embedding model
        print(f"Loading embedding model: {settings.EMBEDDING_MODEL}")
        _models.embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)
        
        # Configure Gemini with explicit API key
        print("Configuring Gemini API...")
        api_key = settings.GEMINI_API_KEY or os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise Exception("GEMINI_API_KEY not found in .env file")
        
        print(f"API Key present: {len(api_key)} characters")
        genai.configure(api_key=api_key)
        
        # List available models and prioritize free-tier friendly models
        print("Checking available models...")
        try:
            # Preferred models in order (best for free tier)
            preferred_models = [
                'gemini-1.5-flash',      # Best for free tier - fast & generous limits
                'gemini-1.5-flash-002',  # Alternate flash version
                'gemini-1.5-pro',        # Pro version (lower limits but still good)
                'gemini-pro',            # Legacy but stable
            ]
            
            available_models = []
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    model_name = m.name.replace('models/', '')
                    available_models.append(model_name)
                    print(f"  ✅ Found: {model_name}")
            
            if not available_models:
                print("❌ No models available with this API key")
                raise Exception("No Gemini models available. Check API key permissions.")
            
            # Select the first preferred model that's available
            model_to_use = None
            for preferred in preferred_models:
                for available in available_models:
                    if preferred in available:
                        model_to_use = available
                        break
                if model_to_use:
                    break
            
            # Fallback to first available if no preferred match
            if not model_to_use:
                model_to_use = available_models[0]
            
            print(f"🎯 Using model: {model_to_use}")
            _models.gemini_model = genai.GenerativeModel(model_to_use)
            
            # Optional test - don't fail if test doesn't work
            print("Testing model connectivity...")
            try:
                test_response = _models.gemini_model.generate_content(
                    "Test: respond with OK",
                    generation_config=genai.types.GenerationConfig(
                        max_output_tokens=20,
                        temperature=0.1,
                    )
                )
                
                # Try to get response text
                response_text = "Model loaded"
                try:
                    response_text = test_response.text
                except:
                    try:
                        if test_response.candidates and len(test_response.candidates) > 0:
                            candidate = test_response.candidates[0]
                            if hasattr(candidate, 'content') and candidate.content.parts:
                                response_text = candidate.content.parts[0].text
                    except:
                        pass
                
                print(f"✅ Model test successful: {response_text}")
            except Exception as test_error:
                # Test failed but model is loaded - continue anyway
                print(f"⚠️  Model test had issues (non-critical): {test_error}")
                print(f"✅ Model initialized - will test during actual use")
            
        except Exception as e:
            print(f"❌ Error with Gemini API: {str(e)}")
            
            # If quota error, provide helpful message
            if "quota" in str(e).lower() or "429" in str(e):
                print("\n⚠️  QUOTA ISSUE DETECTED:")
                print("   - Your API key may have hit daily/minute limits")
                print("   - Try waiting 1-5 minutes and restart")
                print("   - Generate a NEW API key at: https://aistudio.google.com/apikey")
                print("   - Check usage at: https://ai.google.dev/gemini-api/docs/rate-limits")
                print("   - Make sure you're using 'gemini-1.5-flash' for best free tier limits\n")
            
            raise Exception(f"Could not initialize Gemini: {str(e)}")
        
        # Load sentiment analyzer
        print(f"Loading sentiment analyzer: {settings.SENTIMENT_MODEL}")
        _models.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model=settings.SENTIMENT_MODEL,
            device=0 if torch.cuda.is_available() else -1
        )
        
        # Initialize ChromaDB with new syntax
        print("Initializing ChromaDB...")
        _models.chroma_client = chromadb.PersistentClient(
            path=settings.CHROMA_DIR
        )
        
        try:
            _models.collection = _models.chroma_client.create_collection(
                name="financial_reports",
                metadata={"hnsw:space": "cosine"}
            )
        except:
            _models.collection = _models.chroma_client.get_collection(
                name="financial_reports"
            )
    
    return _models