"""
LLM service - Generate answers using Google Gemini
"""

from typing import List, Tuple
import google.generativeai as genai
from app.api.dependencies import ModelDependencies

class LLMService:
    """Handle LLM operations using Gemini"""
    
    def generate_answer(
        self, 
        question: str, 
        chunks: List[str], 
        models: ModelDependencies,
        max_length: int = 500
    ) -> Tuple[str, float]:
        """Generate answer using Gemini API"""
        
        # Combine chunks
        context = "\n\n---\n\n".join(chunks[:5])
        
        # Enhanced prompt to reduce hallucinations
        prompt = f"""You are a financial analyst assistant. Answer the question based ONLY on the provided context from a financial document.

IMPORTANT RULES:
1. Only use information explicitly stated in the context below
2. If the answer is not in the context, say "I cannot find this information in the uploaded document"
3. Cite specific numbers and facts when available
4. Be concise and factual
5. Do not add information from your general knowledge

CONTEXT FROM FINANCIAL REPORT:
{context}

QUESTION: {question}

ANSWER (based only on the context above):"""
        
        try:
            # Generate response with Gemini
            response = models.gemini_model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,  # Low temperature for more factual responses
                    top_p=0.8,
                    top_k=40,
                    max_output_tokens=max_length,
                )
            )
            
            answer = response.text.strip()
            
            # Detect hallucination indicators
            hallucination_indicators = [
                "typically", "usually", "commonly", "in general", 
                "most companies", "industry standard", "it is known that",
                "generally speaking", "as we know"
            ]
            
            confidence = 0.85  # Base confidence for Gemini
            
            if any(indicator in answer.lower() for indicator in hallucination_indicators):
                confidence = 0.5
                answer = f"[Low confidence - may contain general knowledge] {answer}"
            
            # Check if answer admits not finding info
            if any(phrase in answer.lower() for phrase in ["cannot find", "not in the document", "don't have"]):
                confidence = 0.3
            
            return answer, confidence
            
        except Exception as e:
            print(f"Gemini API error: {str(e)}")
            # Fallback response
            return f"Error generating answer: {str(e)}", 0.0
    
    def generate_summary(self, text: str, models: ModelDependencies) -> str:
        """Generate summary using Gemini"""
        
        prompt = f"""Summarize the key financial information from this document in 3-4 sentences.

Document excerpt:
{text[:3000]}

Summary:"""
        
        try:
            response = models.gemini_model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,
                    max_output_tokens=200,
                )
            )
            return response.text.strip()
        except Exception as e:
            print(f"Gemini API error: {str(e)}")
            return "Summary generation failed"