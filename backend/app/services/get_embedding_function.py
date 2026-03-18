import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def get_embedding_function():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")

    return OpenAIEmbeddings(
        model="text-embedding-3-small",     # or "text-embedding-3-large"
        api_key=api_key,
    )