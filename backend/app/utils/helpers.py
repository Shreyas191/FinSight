"""
Helper utility functions
"""

from typing import List
import re

def clean_text(text: str) -> str:
    """Clean and normalize text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

def extract_keywords(text: str, min_length: int = 4) -> List[str]:
    """Extract keywords from text"""
    words = text.lower().split()
    keywords = [w for w in words if len(w) >= min_length]
    return list(set(keywords))

def format_number(num: str) -> str:
    """Format number with commas"""
    try:
        return f"{float(num):,.2f}"
    except:
        return num

def truncate_text(text: str, max_length: int = 150) -> str:
    """Truncate text to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length].rsplit(' ', 1)[0] + '...'

