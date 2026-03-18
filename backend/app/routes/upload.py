from fastapi import APIRouter, File, HTTPException, Query, UploadFile

from app.services.ingest import ingest_documents, ingest_single_file
from app.utils.paths import DATA_DIR

router = APIRouter()


@router.get("/")
def list_uploaded_files():
    files = []
    for file_path in DATA_DIR.glob("*.pdf"):
        files.append(
            {
                "filename": file_path.name,
                "path": str(file_path),
                "size_bytes": file_path.stat().st_size,
            }
        )

    return {"count": len(files), "files": files}


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    ingest: bool = Query(False),
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    save_path = DATA_DIR / file.filename

    if save_path.exists():
        raise HTTPException(status_code=400, detail="A file with this name already exists")

    try:
        content = await file.read()
        save_path.write_bytes(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")

    response = {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "path": str(save_path),
    }

    if ingest:
        try:
            print("Starting ingestion...")
            ingest_single_file(str(save_path))
            print("Ingestion completed successfully")

            response["ingest_result"] = "Ingestion completed successfully"

        except Exception as e:
            print("INGEST ERROR:", str(e))  
            raise HTTPException(
                status_code=500,
                detail=f"File uploaded but ingestion failed: {str(e)}",
            )

    return response


@router.post("/ingest/{filename}")
def ingest_uploaded_file(filename: str):
    file_path = DATA_DIR / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    if file_path.suffix.lower() != ".pdf":
        raise HTTPException(status_code=400, detail="Only PDF files can be ingested")

    try:
        return ingest_single_file(str(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")


@router.post("/ingest-all")
def ingest_all_uploaded_files(reset: bool = Query(False)):
    try:
        return ingest_documents(reset=reset)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bulk ingestion failed: {str(e)}")