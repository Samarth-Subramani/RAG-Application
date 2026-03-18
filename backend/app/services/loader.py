from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader, PyPDFLoader
from langchain_core.documents import Document

from app.utils.paths import DATA_DIR


def load_documents() -> list[Document]:
    document_loader = PyPDFDirectoryLoader(str(DATA_DIR))
    return document_loader.load()

def load_single_document(file_path: str) -> list[Document]:
    loader = PyPDFLoader(file_path)
    return loader.load()