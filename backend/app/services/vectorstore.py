import shutil
from pathlib import Path

from langchain_core.documents import Document
from langchain_chroma import Chroma

from app.services.get_embedding_function import get_embedding_function
from app.utils.paths import CHROMA_DIR


def get_vectorstore() -> Chroma:
    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=get_embedding_function(),
    )


def add_to_chroma(chunks: list[Document]) -> dict:
    db = get_vectorstore()

    existing_items = db.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = []
    for chunk in chunks:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if new_chunks:
        print(f"Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)

        return {
            "message": "Documents added to Chroma",
            "chunks_added": len(new_chunks),
            "existing_documents": len(existing_ids),
        }

    print("No new documents to add")
    return {
        "message": "No new documents to add",
        "chunks_added": 0,
        "existing_documents": len(existing_ids),
    }


def similarity_search(query_text: str, k: int = 5):
    db = get_vectorstore()
    return db.similarity_search_with_score(query_text, k=k)

def clear_database() -> None:
    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)