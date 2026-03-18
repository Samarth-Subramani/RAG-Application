# RAG Chat Application (Python + FastAPI + React + ChromaDB + OpenAI)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/Frontend-React-blue)](https://react.dev/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-purple)](https://www.trychroma.com/)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI-black)](https://openai.com/)

&#x20;  &#x20;

---

## Overview

This is an **end-to-end Retrieval-Augmented Generation (RAG) application** that allows users to:

- Upload PDF documents
- Automatically ingest them into a vector database
- Ask questions in a chat interface
- Get accurate answers grounded in uploaded documents

---

## Architecture

```
React Frontend  →  FastAPI Backend  →  RAG Pipeline
                           ↓
                    Chroma Vector DB
                           ↓
                        OpenAI
```

---

## Features

### Document Handling

- Upload PDF files via UI
- Automatic ingestion into ChromaDB
- Chunking + embedding pipeline

### RAG Pipeline

- Semantic search using ChromaDB
- OpenAI embeddings + LLM
- Context-aware answer generation

### Chat Interface

- Chat-style UI (user ↔ AI)
- Left-right message bubbles
- Loading indicators

### Backend

- FastAPI REST APIs
- Modular architecture (routes + services)
- Real-time ingestion pipeline

---

## Tech Stack

### Backend

- FastAPI
- LangChain
- ChromaDB
- OpenAI API

### Frontend

- React (Vite)
- Fetch API

---

## Project Structure

```
RAG-Application/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   └── utils/
│   ├── data/        # uploaded PDFs
│   └── chroma/      # vector DB 
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── services/
│
└── README.md
```

---

## Setup Instructions

### Install uv

```bash
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone and Install Dependencies

```bash
git clone <repository-url>
cd backend
uv sync --all-extras

# activate environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate  # Windows
```

### Set OpenAI API Key

```
export OPENAI_API_KEY="your_api_key_here"
```

Windows:

```
set OPENAI_API_KEY=your_api_key_here
```

### Running the APP

```
uvicorn app.main:app --reload
```

API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Frontend Setup

```
cd frontend

npm install
npm run dev
```

App runs on: [http://localhost:5173](http://localhost:5173)

---

## How It Works

### Upload Document

```
POST /files/upload?ingest=true
```

- Saves PDF
- Splits into chunks
- Generates embeddings (OpenAI)
- Stores in ChromaDB

---

### Ask Question

```
POST /query/
```

- Query is embedded
- Top-k relevant chunks retrieved
- OpenAI generates answer using context

---

### Response Format

```
{
  "data": {
    "answer": "...",
    "sources": [...]
  }
}
```

---

## Example Workflow

1. Upload a PDF
2. Ask: "Ask questions related to the pdf?"
3. Get an answer grounded in the document

---

## Troubleshooting

### Reset Vector DB

```
rm -rf chroma
```

### Re-ingest documents

```
POST /files/ingest-all
```

### Common Issues

- CORS errors → enable middleware in FastAPI
- No results → ensure ingestion completed
- API key errors → verify OpenAI key

---

## Future Improvements

- File-based query filtering
- Source highlighting in UI
- Streaming responses
- Docker deployment
- Authentication
- Evaluation metrics (RAGAS)

---

## Key Learnings

- End-to-end RAG system design
- Vector search with ChromaDB
- FastAPI + React integration
- OpenAI-powered LLM applications

---

## Author

Samarth Subramani Nagarathna

---

## If you like this project

Give it a star ⭐ and feel free to contribute!

