"""
Shared dependencies and model loading
"""

from sentence_transformers import SentenceTransformer
from transformers import pipeline
import chromadb
from chromadb.config import Settings as ChromaSettings
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
        
        # List available models
        print("Checking available models...")
        try:
            available_models = []
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    available_models.append(m.name)
                    print(f"  ✅ Found: {m.name}")
            
            if not available_models:
                print("❌ No models available with this API key")
                raise Exception("No Gemini models available. Check API key permissions.")
            
            # Use the first available model
            model_to_use = available_models[0]
            print(f"Using model: {model_to_use}")
            _models.gemini_model = genai.GenerativeModel(model_to_use)
            
            # Test it
            print("Testing model...")
            test_response = _models.gemini_model.generate_content("Hello, respond with 'OK'")
            print(f"✅ Model test successful: {test_response.text[:50]}")
            
        except Exception as e:
            print(f"❌ Error with Gemini API: {str(e)}")
            raise Exception(f"Could not initialize Gemini: {str(e)}")
        
        # Load sentiment analyzer
        print(f"Loading sentiment analyzer: {settings.SENTIMENT_MODEL}")
        _models.sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model=settings.SENTIMENT_MODEL,
            device=0 if torch.cuda.is_available() else -1
        )
        
        # Initialize ChromaDB
        print("Initializing ChromaDB...")
        _models.chroma_client = chromadb.Client(ChromaSettings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=settings.CHROMA_DIR
        ))
        
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