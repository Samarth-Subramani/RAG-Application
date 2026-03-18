from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

from app.services.rag import query_rag

router = APIRouter()


class QueryRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User question")
    top_k: int = Field(5, ge=1, le=20, description="Number of chunks to retrieve")


@router.post("/")
def ask_question(payload: QueryRequest):
    query_text = payload.query.strip()

    if not query_text:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        result = query_rag(query_text, k=payload.top_k)
        return {
            "message": "Query processed successfully",
            "data": result,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")