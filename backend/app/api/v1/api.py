from fastapi import APIRouter

from app.api.v1.endpoints import auth, integrations, documents, webhooks, sync_jobs, analytics

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(integrations.router, prefix="/integrations", tags=["integrations"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
api_router.include_router(sync_jobs.router, prefix="/sync-jobs", tags=["sync-jobs"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
