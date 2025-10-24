"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, ConfigDict  # Added ConfigDict
from typing import List, Optional, Dict, Any

class QueryRequest(BaseModel):
    question: str
    top_k: int = 5
    document_ids: Optional[List[str]] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[Dict[str, Any]]
    confidence: float

class ComparisonRequest(BaseModel):
    document_ids: List[str]
    metrics: List[str]

class ComparisonResponse(BaseModel):
    comparison: Dict[str, Dict[str, Any]]
    insights: List[str]

class MetricsResponse(BaseModel):
    revenue: Dict[str, Any]
    profit_margin: Dict[str, Any]
    growth_rate: Dict[str, Any]
    debt_to_equity: Dict[str, Any]
    risk_score: float
    key_metrics: Dict[str, Any]

class ExportRequest(BaseModel):
    document_id: str
    include_summary: bool = True
    include_qa: bool = True
    include_sentiment: bool = True
    include_metrics: bool = True

class DocumentInfo(BaseModel):
    id: str
    filename: str
    upload_date: str
    chunks: int
    sentiment: Dict
    summary: Dict

class UploadResponse(BaseModel):
    document_id: str
    message: str
    chunks: int
    sentiment: Dict
    summary: Dict