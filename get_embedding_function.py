from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from secret_key import huggingface_key

def get_embedding_function():
    
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=huggingface_key, model_name="sentence-transformers/all-MiniLM-l6-v2"
    )
    #print(huggingface_key)
    return embeddings

