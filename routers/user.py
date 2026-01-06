from fastapi import APIRouter,Body,Query
from controllers import users as user_controller
from uuid import UUID
from fastapi import Response
router = APIRouter(
    prefix="/users",
    tags=["users"],
)
@router.post("/login")
def login_user(
    response: Response,
    email: str = Body(..., embed=True),
    password: str = Body(..., embed=True),
):
    token, user = user_controller.login(email, password)

    response.set_cookie(
        key="Token",
        value=token,
        httponly=True,
        secure=False,      # True in production (HTTPS)
        samesite="lax",
        max_age=60 * 30,   # 30 minutes
    )

    return {
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email,
    }


@router.post("/signup" )
def signup_user(
    email: str = Body(..., embed=True),
    password: str = Body(..., embed=True)
):
    return user_controller.signup(email, password)