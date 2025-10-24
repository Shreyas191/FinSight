# 📊 FinSight - AI-Powered Financial Report Analyzer

<div align="center">

![FinSight Banner](https://img.shields.io/badge/FinSight-AI%20Financial%20Analyzer-8B5CF6?style=for-the-badge)

**Intelligent financial document analysis powered by Google Gemini AI, RAG, and advanced NLP**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [API Documentation](#-api-documentation) • [Deployment](#-deployment)

</div>

---

## 🎯 Overview

**FinSight** is an intelligent financial document analysis platform that leverages cutting-edge AI technologies to extract insights from financial reports, annual statements, and business documents. Upload PDFs, ask questions in natural language, and receive AI-powered analysis with sentiment scoring, key metrics extraction, and contextual answers.

### 🌟 Key Capabilities

- 📄 **PDF Processing** - Extract and analyze text from financial documents
- 🤖 **AI-Powered Q&A** - Ask questions and get accurate answers using RAG (Retrieval Augmented Generation)
- 📈 **Sentiment Analysis** - Automatic sentiment scoring of financial content
- 💡 **Smart Extraction** - Auto-extract revenue, profit, EPS, risks, and opportunities
- 📊 **Export Reports** - Generate professional PDF analysis reports
- 🔍 **Vector Search** - Fast semantic search through document chunks using embeddings

---

## ✨ Features

### Backend Capabilities

- ✅ **Google Gemini Integration** - State-of-the-art LLM for answer generation
- ✅ **RAG Architecture** - Retrieval Augmented Generation for accurate, grounded responses
- ✅ **Vector Database** - ChromaDB for efficient semantic search
- ✅ **Sentiment Analysis** - DistilBERT-based sentiment scoring
- ✅ **Smart Chunking** - Intelligent text splitting with overlap for better context
- ✅ **Automatic Metrics Extraction** - Regex-based financial metric detection
- ✅ **PDF Export** - Generate professional analysis reports
- ✅ **Multi-Document Support** - Manage and query multiple documents
- ✅ **Q&A History** - Track questions and answers per document

### Frontend Features

- ✅ **Modern UI** - Clean, responsive design with Tailwind CSS
- ✅ **Drag & Drop Upload** - Easy PDF upload interface
- ✅ **Real-time Analysis** - Live sentiment and metrics display
- ✅ **Interactive Chat** - Natural conversation with your documents
- ✅ **Document Management** - View, select, and delete uploaded documents
- ✅ **Confidence Scoring** - Visual confidence indicators for answers
- ✅ **Export Reports** - Download comprehensive PDF analysis

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (React)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Upload  │  │   Chat   │  │ Document │  │  Export  │   │
│  │   UI     │  │    UI    │  │   List   │  │    UI    │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↕ HTTP/REST API
┌─────────────────────────────────────────────────────────────┐
│                      Backend (FastAPI)                       │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                    API Routes                         │  │
│  │  /upload  /query  /documents  /export  /delete       │  │
│  └──────────────────────────────────────────────────────┘  │
│                            ↕                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                  Service Layer                        │  │
│  │  • PDF Service     • LLM Service                      │  │
│  │  • Embedding Svc   • Sentiment Service                │  │
│  │  • Export Service                                     │  │
│  └──────────────────────────────────────────────────────┘  │
│                            ↕                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   AI Models                           │  │
│  │  • Google Gemini (LLM)                                │  │
│  │  • SentenceTransformer (Embeddings)                   │  │
│  │  • DistilBERT (Sentiment)                             │  │
│  │  • ChromaDB (Vector Store)                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Tech Stack

#### Backend
- **Framework:** FastAPI
- **LLM:** Google Gemini 1.5 Flash/Pro
- **Embeddings:** SentenceTransformers (all-MiniLM-L6-v2)
- **Sentiment:** DistilBERT (SST-2 fine-tuned)
- **Vector DB:** ChromaDB
- **PDF Processing:** PyPDF2, LangChain
- **Export:** ReportLab

#### Frontend
- **Framework:** React 18+
- **Styling:** Tailwind CSS
- **Icons:** Lucide React
- **HTTP Client:** Fetch API
- **Build Tool:** Vite/Create React App

---

## 🚀 Installation

### Prerequisites

- Python 3.11+
- Node.js 18+
- Google Gemini API Key ([Get one here](https://aistudio.google.com/apikey))
- 4GB+ RAM (for ML models)

### Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/finsight.git
cd finsight/backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cat > .env << EOF
GEMINI_API_KEY=your_gemini_api_key_here
HOST=0.0.0.0
PORT=8000
DEBUG=True
EOF

# 5. Create required directories
mkdir -p uploads exports chroma_db

# 6. Run the backend
python run.py
```

Backend will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

### Frontend Setup

```bash
# 1. Navigate to frontend directory
cd ../frontend

# 2. Install dependencies
npm install

# 3. Create .env file
cat > .env << EOF
REACT_APP_API_URL=http://localhost:8000
EOF

# 4. Start development server
npm start
```

Frontend will be available at: `http://localhost:3000`

---

## 📖 Usage

### 1. Start the Application

```bash
# Terminal 1 - Backend
cd backend
python run.py

# Terminal 2 - Frontend
cd frontend
npm start
```

### 2. Upload a Financial Report

1. Open `http://localhost:3000`
2. Click **"Upload PDF"** or drag & drop a financial report
3. Wait for processing (10-30 seconds for large documents)
4. View auto-extracted metrics and sentiment

### 3. Ask Questions

```
Examples:
- "What is the total revenue for 2024?"
- "Give me the financial details of the company"
- "What are the main risks mentioned?"
- "What is the profit margin?"
- "Analyze the company's growth opportunities"
- "What is the earnings per share?"
```

### 4. Export Analysis

1. Click **"Export Report"**
2. Select document and report options
3. Download comprehensive PDF analysis

---

## 🔧 Configuration

### Backend Configuration (`backend/.env`)

```env
# API Keys
GEMINI_API_KEY=your_key_here

# Server Settings
HOST=0.0.0.0
PORT=8000
DEBUG=True

# Model Configuration
EMBEDDING_MODEL=all-MiniLM-L6-v2
SENTIMENT_MODEL=distilbert-base-uncased-finetuned-sst-2-english
GEMINI_MODEL=gemini-1.5-flash

# Processing Settings
CHUNK_SIZE=1000
CHUNK_OVERLAP=100
MAX_CHUNKS_PER_QUERY=5

# Storage Directories
UPLOAD_DIR=uploads
EXPORT_DIR=exports
CHROMA_DIR=chroma_db
```

### Frontend Configuration (`frontend/.env`)

```env
REACT_APP_API_URL=http://localhost:8000
REACT_APP_MAX_FILE_SIZE=10485760  # 10MB
```

---

## 📚 API Documentation

### Endpoints

#### `POST /upload`
Upload and process a PDF document.

**Request:**
```bash
curl -X POST "http://localhost:8000/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@financial_report.pdf"
```

**Response:**
```json
{
  "document_id": "doc_20241024_123456",
  "message": "PDF processed successfully",
  "chunks": 45,
  "sentiment": {
    "overall": "positive",
    "score": 0.72,
    "breakdown": {
      "positive": 65.5,
      "neutral": 28.3,
      "negative": 6.2
    }
  },
  "summary": {
    "revenue": "2.5 billion",
    "profit": "450 million",
    "profitMargin": "18%",
    "eps": "3.75",
    "key_risks": ["Market volatility", "..."],
    "opportunities": ["Strategic expansion", "..."]
  }
}
```

#### `POST /query`
Ask questions about uploaded documents.

**Request:**
```json
{
  "question": "What is the total revenue?",
  "top_k": 5,
  "document_ids": ["doc_20241024_123456"]
}
```

**Response:**
```json
{
  "answer": "The total revenue for 2024 is $2.5 billion...",
  "sources": [
    {
      "document": "financial_report.pdf",
      "chunk": 3,
      "doc_id": "doc_20241024_123456"
    }
  ],
  "confidence": 0.85
}
```

#### `GET /documents`
List all uploaded documents.

**Response:**
```json
[
  {
    "id": "doc_20241024_123456",
    "filename": "financial_report.pdf",
    "upload_date": "2024-10-24T12:34:56",
    "chunks": 45,
    "sentiment": {...},
    "summary": {...}
  }
]
```

#### `DELETE /document/{document_id}`
Delete a document.

#### `POST /export`
Export analysis as PDF.

**Request:**
```json
{
  "document_id": "doc_20241024_123456",
  "include_summary": true,
  "include_qa": true,
  "include_sentiment": true,
  "include_metrics": true
}
```

**Full API Documentation:** Visit `http://localhost:8000/docs` (Swagger UI)

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Test with Sample Document

Generate a test PDF using the included generator:
```bash
python scripts/generate_sample_report.py
```

Or use the web-based generator (included in frontend).

---

## 🐳 Docker Deployment

### Using Docker Compose

```bash
# 1. Create docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    volumes:
      - ./backend/uploads:/app/uploads
      - ./backend/exports:/app/exports
      - ./backend/chroma_db:/app/chroma_db

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    depends_on:
      - backend
EOF

# 2. Run
docker-compose up --build
```

### Backend Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create directories
RUN mkdir -p uploads exports chroma_db

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🌐 Deployment

### Free Deployment Options

#### Option 1: Hugging Face Spaces (Recommended)
- **Pros:** 16GB RAM, supports ML models, completely free
- **Setup:** See [Deployment Guide](DEPLOYMENT.md)

```bash
# Deploy to Hugging Face
git clone https://huggingface.co/spaces/YOUR_USERNAME/finsight
cp -r backend/* finsight/
cd finsight
git add .
git commit -m "Deploy"
git push
```

#### Option 2: Railway + Vercel
- **Backend:** Railway ($5 credit/month)
- **Frontend:** Vercel (free)

```bash
# Deploy backend to Railway
railway login
railway init
railway up

# Deploy frontend to Vercel
cd frontend
vercel
```

#### Option 3: Render
- **Pros:** Easy setup, auto-deploy from GitHub
- **Cons:** 512MB RAM (may need to upgrade)

---

## 📁 Project Structure

```
finsight/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py      # Model loading & DI
│   │   │   └── routes.py            # API endpoints
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── pdf_service.py       # PDF processing
│   │   │   ├── embedding_service.py # Embeddings & vector DB
│   │   │   ├── llm_service.py       # Gemini integration
│   │   │   ├── sentiment_service.py # Sentiment analysis
│   │   │   └── export_service.py    # PDF export
│   │   ├── utils/
│   │   │   └── helpers.py           # Utility functions
│   │   ├── __init__.py
│   │   ├── config.py                # Configuration
│   │   ├── main.py                  # FastAPI app
│   │   └── models.py                # Pydantic models
│   ├── uploads/                     # Uploaded PDFs
│   ├── exports/                     # Generated reports
│   ├── chroma_db/                   # Vector database
│   ├── .env                         # Environment variables
│   ├── .gitignore
│   ├── requirements.txt
│   ├── Dockerfile
│   └── run.py                       # Entry point
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Upload.jsx
│   │   │   ├── Chat.jsx
│   │   │   ├── DocumentList.jsx
│   │   │   └── Export.jsx
│   │   ├── services/
│   │   │   └── api.js               # API client
│   │   ├── App.jsx
│   │   └── index.js
│   ├── .env
│   ├── package.json
│   ├── tailwind.config.js
│   └── Dockerfile
│
├── docker-compose.yml
├── README.md
├── LICENSE
└── DEPLOYMENT.md
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint/Prettier for JavaScript
- Write tests for new features
- Update documentation

---

## 🐛 Troubleshooting

### Backend Issues

**Problem:** "Gemini API quota exceeded"
```bash
# Solution: Wait 1-5 minutes or generate new API key
# Check usage: https://ai.google.dev/gemini-api/docs/rate-limits
```

**Problem:** "Out of memory"
```bash
# Solution: Reduce model sizes or use Gemini API for embeddings
# Edit config.py: EMBEDDING_MODEL = "gemini"  # Use Gemini for embeddings
```

**Problem:** "ChromaDB deprecated configuration"
```bash
# Already fixed in latest version
# Use: chromadb.PersistentClient(path="chroma_db")
```

### Frontend Issues

**Problem:** "CORS error"
```bash
# Solution: Check backend CORS settings in main.py
# Ensure frontend URL is in allow_origins
```

**Problem:** "API connection refused"
```bash
# Solution: Verify backend is running on correct port
# Check REACT_APP_API_URL in .env
```

---

## 📊 Performance

- **Upload Processing:** 10-30 seconds for 50-page document
- **Query Response:** 1-3 seconds
- **Embedding Generation:** ~0.5 seconds per chunk
- **Sentiment Analysis:** ~2 seconds for 30 chunks

### Optimization Tips

1. Use `gemini-1.5-flash` for faster responses
2. Reduce `CHUNK_SIZE` for faster processing
3. Enable GPU for local inference (PyTorch)
4. Cache embeddings for repeated queries

---

## 🔒 Security

- ✅ API key stored in environment variables
- ✅ File upload validation (PDF only)
- ✅ Input sanitization
- ✅ CORS protection
- ⚠️ Add authentication for production use
- ⚠️ Implement rate limiting
- ⚠️ Add HTTPS in production

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) - Advanced LLM capabilities
- [Hugging Face](https://huggingface.co/) - Transformers and models
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/finsight/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/finsight/discussions)
- **Email:** your.email@example.com

---

## 🗺️ Roadmap

- [ ] Multi-language support
- [ ] Real-time collaboration
- [ ] Advanced visualizations (charts, graphs)
- [ ] Comparison mode (multiple documents)
- [ ] Export to Excel/CSV
- [ ] Mobile app
- [ ] API authentication & rate limiting
- [ ] Custom fine-tuned models
- [ ] Integration with financial data APIs

---

<div align="center">

**Made with ❤️ by [Your Name]**

⭐ Star this repo if you find it helpful!

[Report Bug](https://github.com/yourusername/finsight/issues) · [Request Feature](https://github.com/yourusername/finsight/issues)

</div>
