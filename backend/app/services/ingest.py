from app.services.loader import load_documents, load_single_document
from app.services.chunking import split_documents, calculate_chunk_ids
from app.services.vectorstore import add_to_chroma, clear_database


def ingest_documents(reset: bool = False) -> dict:
    if reset:
        print("Clearing Database")
        clear_database()

    documents = load_documents()
    chunks = split_documents(documents)
    chunks_with_ids = calculate_chunk_ids(chunks)
    result = add_to_chroma(chunks_with_ids)

    return {
        "documents_loaded": len(documents),
        "chunks_created": len(chunks_with_ids),
        **result,
    }

def ingest_single_file(file_path: str) -> dict:
    documents = load_single_document(file_path)
    chunks = split_documents(documents)
    chunks_with_ids = calculate_chunk_ids(chunks)
    result = add_to_chroma(chunks_with_ids)

    return {
        "file_path": file_path,
        "documents_loaded": len(documents),
        "chunks_created": len(chunks_with_ids),
        **result,
    }