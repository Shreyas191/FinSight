"""
FastAPI application initialization and startup
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.routes import router
from app.api.dependencies import get_models, ModelDependencies

# Initialize FastAPI app
app = FastAPI(
    title="Financial Report Analyzer API",
    description="AI-powered financial document analysis with RAG (Gemini-powered)",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)

# Startup event - load models
@app.on_event("startup")
async def startup_event():
    """Load AI models on startup"""
    print("🚀 Starting Financial Report Analyzer Backend...")
    print(f"📊 Server: {settings.HOST}:{settings.PORT}")
    print(f"🤖 Powered by: Google Gemini")
    print(f"🔧 Loading AI models...")
    
    try:
        models = get_models()
        print("✅ All models loaded successfully!")
        print(f"✅ Gemini model: {settings.GEMINI_MODEL}")
    except Exception as e:
        print(f"❌ Error loading models: {e}")
        raise

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Financial Report Analyzer API",
        "version": "2.0.0",
        "llm": "Google Gemini",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    models = get_models()
    return {
        "status": "healthy",
        "llm": "Gemini",
        "models_loaded": all([
            models.embedding_model is not None,
            models.gemini_model is not None,
            models.sentiment_analyzer is not None,
            models.collection is not None
        ]),
        "documents_loaded": len(models.document_store)
    }