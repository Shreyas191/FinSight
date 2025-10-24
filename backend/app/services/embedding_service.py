"""
Embedding service - Generate and store embeddings
"""

from typing import List, Optional
from app.api.dependencies import ModelDependencies

class EmbeddingService:
    """Handle embedding operations"""
    
    def generate_embeddings(self, texts: List[str], models: ModelDependencies) -> List[List[float]]:
        """Generate embeddings for texts"""
        embeddings = models.embedding_model.encode(texts).tolist()
        return embeddings
    
    def store_embeddings(
        self, 
        doc_id: str, 
        chunks: List[str], 
        embeddings: List[List[float]], 
        filename: str,
        models: ModelDependencies
    ):
        """Store embeddings in vector database"""
        models.collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"{doc_id}_chunk_{i}" for i in range(len(chunks))],
            metadatas=[{
                "source": filename,
                "chunk_id": i,
                "doc_id": doc_id
            } for i in range(len(chunks))]
        )
    
    def retrieve_chunks(
        self,
        query_embedding: List[float],
        top_k: int,
        document_ids: Optional[List[str]],
        models: ModelDependencies
    ):
        """Retrieve relevant chunks from vector database"""
        where_filter = None
        if document_ids:
            where_filter = {"doc_id": {"$in": document_ids}}
        
        results = models.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_filter
        )
        
        return results