import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.services.vectorstore import similarity_search

load_dotenv()

PROMPT_TEMPLATE = """
You are answering a user question using only the provided context.

Question:
{question}

Context:
{context}

Instructions:
- Answer only from the provided context.
- If the context is not enough, say that the answer is not available in the documents.
- Be clear and concise.
"""

def build_prompt(query_text: str, results) -> str:
    context_text = "\n\n-------------\n\n".join(
        [doc.page_content for doc, _score in results]
    )

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    return prompt_template.format(
        question=query_text,
        context=context_text,
    )


def get_llm() -> ChatOpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in environment variables.")

    return ChatOpenAI(
        model="gpt-4o",
        temperature=0.2,
        api_key=api_key,
    )


def query_rag(query_text: str, k: int = 5) -> dict:
    results = similarity_search(query_text, k=k)

    if not results:
        return {
            "query": query_text,
            "answer": "No relevant documents were found in the knowledge base.",
            "sources": [],
        }
    
    prompt = build_prompt(query_text, results)

    llm = get_llm()
    response = llm.invoke(prompt)

    sources = []
    for doc, score in results:
        sources.append(
            {
                "id": doc.metadata.get("id"),
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page"),
                "score": score,
                "content": doc.page_content,
            }
        )

    return {
        "query": query_text,
        "answer": response.content if hasattr(response, "content") else str(response),
        "sources": sources,
    }