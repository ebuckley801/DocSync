from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_documents():
    return {"message": "List documents endpoint"}


@router.get("/{document_id}")
async def get_document(document_id: int):
    return {"message": f"Get document {document_id} endpoint"}


@router.get("/search")
async def search_documents():
    return {"message": "Search documents endpoint"}


@router.delete("/{document_id}")
async def delete_document(document_id: int):
    return {"message": f"Delete document {document_id} endpoint"}
