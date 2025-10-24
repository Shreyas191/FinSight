"""
PDF processing service - Extract text and metadata
"""

import PyPDF2
import re
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import settings

class PDFService:
    """Handle PDF operations"""
    
    def extract_text(self, pdf_path: str) -> str:
        """Extract text from PDF file"""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            raise Exception(f"Failed to extract text from PDF: {str(e)}")
    
    def chunk_text(self, text: str) -> List[str]:
        """Split text into chunks"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        chunks = text_splitter.split_text(text)
        return chunks
    
    def extract_financial_metrics(self, text: str) -> Dict[str, str]:
        """Extract financial metrics using regex"""
        metrics = {
            "revenue": None,
            "net_income": None,
            "profit_margin": None,
            "eps": None
        }
        
        text_lower = text.lower()
        
        # Revenue patterns
        revenue_patterns = [
            r"(?:total\s+)?revenue[s]?\s+(?:of\s+)?\$?([\d,]+\.?\d*)\s*(?:million|billion|M|B)?",
            r"net\s+(?:sales|revenues?)\s+(?:of\s+)?\$?([\d,]+\.?\d*)\s*(?:million|billion|M|B)?"
        ]
        
        for pattern in revenue_patterns:
            match = re.search(pattern, text_lower, re.IGNORECASE)
            if match:
                metrics["revenue"] = match.group(1)
                break
        
        # Net income patterns
        income_patterns = [
            r"net\s+income\s+(?:of\s+)?\$?([\d,]+\.?\d*)\s*(?:million|billion|M|B)?",
            r"net\s+(?:profit|earnings?)\s+(?:of\s+)?\$?([\d,]+\.?\d*)\s*(?:million|billion|M|B)?"
        ]
        
        for pattern in income_patterns:
            match = re.search(pattern, text_lower, re.IGNORECASE)
            if match:
                metrics["net_income"] = match.group(1)
                break
        
        # EPS patterns
        eps_patterns = [
            r"earnings?\s+per\s+share\s+(?:of\s+)?\$?([\d,]+\.?\d*)",
            r"EPS\s+(?:of\s+)?\$?([\d,]+\.?\d*)"
        ]
        
        for pattern in eps_patterns:
            match = re.search(pattern, text_lower, re.IGNORECASE)
            if match:
                metrics["eps"] = match.group(1)
                break
        
        # Calculate profit margin
        if metrics["revenue"] and metrics["net_income"]:
            try:
                rev = float(metrics["revenue"].replace(",", ""))
                inc = float(metrics["net_income"].replace(",", ""))
                metrics["profit_margin"] = f"{(inc/rev)*100:.2f}%"
            except:
                pass
        
        return metrics
    
    def extract_summary(self, chunks: List[str], full_text: str) -> Dict:
        """Extract comprehensive financial summary"""
        metrics = self.extract_financial_metrics(full_text)
        
        # Extract risks
        risk_keywords = ["risk", "challenge", "threat", "uncertainty", "volatility"]
        risks = []
        
        for chunk in chunks[:20]:
            chunk_lower = chunk.lower()
            if any(keyword in chunk_lower for keyword in risk_keywords):
                sentences = chunk.split('.')
                for sentence in sentences:
                    if any(kw in sentence.lower() for kw in risk_keywords) and len(sentence.strip()) > 20:
                        risks.append(sentence.strip()[:150])
                        if len(risks) >= 5:
                            break
            if len(risks) >= 5:
                break
        
        # Extract opportunities
        opp_keywords = ["opportunity", "growth", "expansion", "innovation", "strategic"]
        opportunities = []
        
        for chunk in chunks[:20]:
            chunk_lower = chunk.lower()
            if any(keyword in chunk_lower for keyword in opp_keywords):
                sentences = chunk.split('.')
                for sentence in sentences:
                    if any(kw in sentence.lower() for kw in opp_keywords) and len(sentence.strip()) > 20:
                        opportunities.append(sentence.strip()[:150])
                        if len(opportunities) >= 5:
                            break
            if len(opportunities) >= 5:
                break
        
        return {
            "revenue": metrics.get("revenue", "Not found"),
            "profit": metrics.get("net_income", "Not found"),
            "profitMargin": metrics.get("profit_margin", "Not found"),
            "eps": metrics.get("eps", "Not found"),
            "key_risks": risks[:5] if risks else ["Market conditions", "Regulatory changes"],
            "opportunities": opportunities[:5] if opportunities else ["Market expansion", "Innovation"]
        }