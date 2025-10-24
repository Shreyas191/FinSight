"""
Sentiment analysis service
"""

from typing import List, Dict
from app.api.dependencies import ModelDependencies

class SentimentService:
    """Handle sentiment analysis"""
    
    def analyze_batch(self, texts: List[str], models: ModelDependencies) -> Dict:
        """Analyze sentiment of multiple text chunks"""
        
        # Truncate texts for model
        truncated_texts = [text[:512] for text in texts]
        
        # Run sentiment analysis
        results = models.sentiment_analyzer(truncated_texts)
        
        # Aggregate results
        positive_count = sum(1 for r in results if r['label'] == 'POSITIVE')
        negative_count = sum(1 for r in results if r['label'] == 'NEGATIVE')
        total = len(results)
        
        positive_pct = (positive_count / total) * 100
        negative_pct = (negative_count / total) * 100
        neutral_pct = 100 - positive_pct - negative_pct
        
        # Calculate average score
        avg_score = sum(
            r['score'] if r['label'] == 'POSITIVE' else (1 - r['score']) 
            for r in results
        ) / total
        
        # Determine overall sentiment
        if positive_pct > 50:
            overall = "positive"
        elif negative_pct > 30:
            overall = "negative"
        else:
            overall = "neutral"
        
        return {
            "overall": overall,
            "score": avg_score,
            "breakdown": {
                "positive": round(positive_pct, 1),
                "neutral": round(neutral_pct, 1),
                "negative": round(negative_pct, 1)
            }
        }