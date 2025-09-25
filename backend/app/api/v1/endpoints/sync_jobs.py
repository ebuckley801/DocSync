from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_sync_jobs():
    return {"message": "List sync jobs endpoint"}


@router.get("/{job_id}")
async def get_sync_job(job_id: int):
    return {"message": f"Get sync job {job_id} endpoint"}


@router.post("/{job_id}/retry")
async def retry_sync_job(job_id: int):
    return {"message": f"Retry sync job {job_id} endpoint"}


@router.delete("/{job_id}")
async def cancel_sync_job(job_id: int):
    return {"message": f"Cancel sync job {job_id} endpoint"}
