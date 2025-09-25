from fastapi import APIRouter

router = APIRouter()


@router.get("/overview")
async def get_overview():
    return {"message": "Analytics overview endpoint"}


@router.get("/sync-frequency")
async def get_sync_frequency():
    return {"message": "Sync frequency metrics endpoint"}


@router.get("/document-changes")
async def get_document_changes():
    return {"message": "Document changes tracking endpoint"}
