from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register():
    return {"message": "User registration endpoint"}


@router.post("/login")
async def login():
    return {"message": "User login endpoint"}


@router.post("/refresh")
async def refresh_token():
    return {"message": "Token refresh endpoint"}


@router.delete("/logout")
async def logout():
    return {"message": "User logout endpoint"}


@router.get("/me")
async def get_current_user():
    return {"message": "Current user info endpoint"}
