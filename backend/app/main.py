from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import router as health_router
from app.routes.upload import router as upload_router
from app.routes.query import router as query_router

app = FastAPI(title="RAG Application API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="/health", tags=["Health"])
app.include_router(upload_router, prefix="/files", tags=["Files"])
app.include_router(query_router, prefix="/query", tags=["Query"])


@app.get("/")
def root():
    return {"message": "RAG FastAPI backend is running"}