"""
API route handlers
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from typing import List
from datetime import datetime
from pathlib import Path

from app.models import (
    QueryRequest, QueryResponse, ComparisonRequest, ComparisonResponse,
    ExportRequest, DocumentInfo, UploadResponse, MetricsResponse
)
from app.api.dependencies import get_models
from app.services.pdf_service import PDFService
from app.services.embedding_service import EmbeddingService
from app.services.llm_service import LLMService
from app.services.sentiment_service import SentimentService
from app.services.export_service import ExportService
from app.config import settings

router = APIRouter()

# Initialize services
pdf_service = PDFService()
embedding_service = EmbeddingService()
llm_service = LLMService()
sentiment_service = SentimentService()
export_service = ExportService()

@router.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """Upload and process PDF file"""
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    models = get_models()
    doc_id = f"doc_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    file_path = Path(settings.UPLOAD_DIR) / f"{doc_id}_{file.filename}"
    
    # Save file
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    try:
        # Extract text
        text = pdf_service.extract_text(str(file_path))
        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from PDF")
        
        # Chunk text
        chunks = pdf_service.chunk_text(text)
        
        # Generate embeddings
        embeddings = embedding_service.generate_embeddings(chunks, models)
        
        # Store in vector database
        embedding_service.store_embeddings(
            doc_id, chunks, embeddings, file.filename, models
        )
        
        # Analyze sentiment
        sentiment = sentiment_service.analyze_batch(chunks[:30], models)
        
        # Extract summary
        summary = pdf_service.extract_summary(chunks, text)
        
        # Store document info
        models.document_store[doc_id] = {
            "id": doc_id,
            "filename": file.filename,
            "upload_date": datetime.now().isoformat(),
            "chunks": len(chunks),
            "sentiment": sentiment,
            "summary": summary,
            "full_text": text,
            "qa_history": []
        }
        
        return UploadResponse(
            document_id=doc_id,
            message="PDF processed successfully",
            chunks=len(chunks),
            sentiment=sentiment,
            summary=summary
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

@router.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    """Query documents using RAG"""
    models = get_models()
    
    try:
        # Generate query embedding
        query_embedding = embedding_service.generate_embeddings(
            [request.question], models
        )[0]
        
        # Retrieve relevant chunks
        results = embedding_service.retrieve_chunks(
            query_embedding, request.top_k, request.document_ids, models
        )
        
        if not results['documents'][0]:
            return QueryResponse(
                answer="No relevant information found. Please upload a document first.",
                sources=[],
                confidence=0.0
            )
        
        # Generate answer
        answer, confidence = llm_service.generate_answer(
            request.question, results['documents'][0], models
        )
        
        # Format sources
        sources = []
        for meta in results['metadatas'][0]:
            doc_id = meta.get('doc_id', 'unknown')
            doc_info = models.document_store.get(doc_id, {})
            sources.append({
                "document": doc_info.get('filename', 'Unknown'),
                "chunk": meta.get('chunk_id', 0),
                "doc_id": doc_id
            })
        
        # Store Q&A history
        for doc_id in set(s['doc_id'] for s in sources):
            if doc_id in models.document_store:
                models.document_store[doc_id]['qa_history'].append({
                    "question": request.question,
                    "answer": answer,
                    "timestamp": datetime.now().isoformat()
                })
        
        return QueryResponse(
            answer=answer,
            sources=sources,
            confidence=confidence
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error querying document: {str(e)}")

@router.get("/documents", response_model=List[DocumentInfo])
async def list_documents():
    """List all uploaded documents"""
    models = get_models()
    return [
        DocumentInfo(
            id=doc_id,
            filename=doc['filename'],
            upload_date=doc['upload_date'],
            chunks=doc['chunks'],
            sentiment=doc['sentiment'],
            summary=doc['summary']
        )
        for doc_id, doc in models.document_store.items()
    ]

@router.delete("/document/{document_id}")
async def delete_document(document_id: str):
    """Delete a document"""
    models = get_models()
    
    if document_id not in models.document_store:
        raise HTTPException(status_code=404, detail="Document not found")
    
    # Delete from vector store
    models.collection.delete(where={"doc_id": document_id})
    
    # Delete from document store
    del models.document_store[document_id]
    
    return {"message": "Document deleted successfully"}

@router.post("/export")
async def export_report(request: ExportRequest):
    """Export analysis as PDF"""
    models = get_models()
    
    if request.document_id not in models.document_store:
        raise HTTPException(status_code=404, detail="Document not found")
    
    doc = models.document_store[request.document_id]
    
    pdf_path = export_service.create_report(
        request.document_id, doc, request, models
    )
    
    return FileResponse(
        pdf_path,
        media_type='application/pdf',
        filename=f"{request.document_id}_analysis.pdf"
    )