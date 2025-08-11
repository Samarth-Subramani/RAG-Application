import argparse
from langchain.vectorstores.chroma import Chroma
from langchain import PromptTemplate, LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from secret_key import huggingface_key
from get_embedding_function import get_embedding_function


CHROMA_PATH= "chroma"

PROMPT_TEMPLATE= """
Query:
{Question}

----

Answer based on the chunks that best match the query:
{Context}
"""

def main():
    #creat a input query.
    parser= argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="Query Text.")
    args = parser.parse_args()
    query_text= args.query_text
    
    
    rag_query(query_text)
    

def rag_query(query_text: str):

    # Redefine the same embedding function
    embedding_function = get_embedding_function()
    db= Chroma(
        persist_directory=CHROMA_PATH, embedding_function=embedding_function
    )

    # Search query in the database to find k most similar chunks
    result= db.similarity_search_with_score(query_text, k=5)
    #results= db.cosine_similarity(query_text, k=5)

    # Create a final prompt with relevant context and query to pass to the LLM.
    context_text= "\n\n-------------\n\n".join([doc.page_content for doc, _score in result])
    prompt_template= ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt=prompt_template.format(Question= query_text, Context= context_text)


    repo_id="mistralai/Mistral-7B-Instruct-v0.3"
    token=huggingface_key


    llm=HuggingFaceEndpoint(
        repo_id=repo_id,
        max_length=128,
        temperature=0.5,
        token=token)

    response_text= llm.invoke(prompt)
    sources = [doc.metadata.get("id", None) for doc, _score in result]
    formatted_response = f"Response: {response_text}\n\n\n\nSources: {sources}"
    print(formatted_response)
    return(response_text)


if __name__=="__main__":
    main()

