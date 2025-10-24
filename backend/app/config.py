"""
Configuration settings loaded from environment variables
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # API Keys
    GEMINI_API_KEY: str = ""
    
    # Models
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    SENTIMENT_MODEL: str = "distilbert-base-uncased-finetuned-sst-2-english"
    GEMINI_MODEL: str = "gemini-1.5-flash"
    
    # Processing
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 100
    MAX_CHUNKS_PER_QUERY: int = 5
    
    # Directories
    UPLOAD_DIR: str = "uploads"
    EXPORT_DIR: str = "exports"
    CHROMA_DIR: str = "chroma_db"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

# Global settings instance
settings = Settings()

# Validate API key
if not settings.GEMINI_API_KEY:
    print("⚠️  WARNING: GEMINI_API_KEY not set in .env file")

# Create directories
Path(settings.UPLOAD_DIR).mkdir(exist_ok=True)
Path(settings.EXPORT_DIR).mkdir(exist_ok=True)
Path(settings.CHROMA_DIR).mkdir(exist_ok=True)