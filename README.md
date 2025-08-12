# RAG Application (Hugging Face + ChromaDB)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/)
[![HuggingFace](https://img.shields.io/badge/Models-HuggingFace-orange)](https://huggingface.co/)
[![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)](https://www.trychroma.com/)

A minimal, reproducible Retrieval-Augmented Generation (RAG) pipeline built with **Hugging Face** models and **ChromaDB** for embeddings + vector search.

It lets you:
- Ingest your own documents into a local ChromaDB collection
- Embed chunks with a Hugging Face embedding model
- Retrieve top-k relevant chunks for a query
- Generate grounded answers with a Hugging Face LLM

---

## Features

- **Local-first** vector DB with Chroma (no cloud dependency)
- **Pluggable embeddings** via `get_embedding_function.py`
- **Simple data ingestion** from the `Data/` folder
- **RAG querying** with source-aware responses
- **Pure Python** scripts (plus a demo notebook)

---

## Quickstart

### 1) Environment

Python 3.10+ recommended
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -U pip
pip install -U chromadb sentence-transformers transformers accelerate torch huggingface-hub langchain 


### 2) Configure embeddings
Open get_embedding_function.py and set your preferred embedding model

### 3) Add your data
Drop your files into the Data/ directory.

### 4) Build the vector store
python populate_data.py

This will:

Load and chunk texts from Data/
Compute embeddings
Store them in a local Chroma collection under ./chroma

### 5) Ask questions (RAG)
python rag_query.py --query ".............?"

optionally
--k 4                    # number of retrieved chunks
--collection my_docs     # custom collection name
--temperature 0.2        # generation temperature

## Configuration

While using:

### Hugging Face Inference API: 
Set HUGGINGFACEHUB_API_TOKEN in your environment, or put it in secret_key.py and import it where needed.
### Local models: 
Ensure transformers, accelerate, and the right backend (CPU/GPU) are set up.

## Model choices
### Embeddings: 
Any Sentence Transformers model works (e.g., all-MiniLM-L6-v2, multi-qa-MiniLM-L6-cos-v1, e5-small-v2, etc.)

### Generator: 
Choose a HF text-generation model that fits your hardware (e.g., mistralai, llama-8b, etc.). CPU-only? Prefer smaller models.

## How it works (RAG flow)
Chunk & Embed – populate_data.py splits your documents and converts them to vectors using get_embedding_function.py.
Upsert to Chroma – vectors + metadata are stored locally under ./chroma.
Retrieve – rag_query.py encodes your query and retrieves the top-k nearest chunks.
Generate – the retrieved context is fed to a HF LLM to produce a grounded answer.

## Troubleshooting
No results / empty answers: verify you ran populate_data.py after adding files to Data/.
Slow generation: switch to a smaller HF model or run with GPU.
Vector store reset: delete the chroma/ folder and re-run ingestion.
Model not found: run huggingface-cli login or ensure the model is public.

## Roadmap
PDF/HTML loaders with clean text extraction
Source highlighting in answers
Eval harness for retrieval quality
Simple API or Streamlit UI
Caching, reranking, and better prompts
