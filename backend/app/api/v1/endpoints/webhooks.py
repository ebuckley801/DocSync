from fastapi import APIRouter

router = APIRouter()


@router.post("/github/{integration_id}")
async def github_webhook(integration_id: int):
    return {"message": f"GitHub webhook for integration {integration_id}"}


@router.post("/notion/{integration_id}")
async def notion_webhook(integration_id: int):
    return {"message": f"Notion webhook for integration {integration_id}"}


@router.post("/confluence/{integration_id}")
async def confluence_webhook(integration_id: int):
    return {"message": f"Confluence webhook for integration {integration_id}"}
