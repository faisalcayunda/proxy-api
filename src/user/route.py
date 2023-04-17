from fastapi import APIRouter, Form
from src.dependencies import config
from src.response import Response
from src.auth.service import create_jwt
import requests
from pydantic import EmailStr
from fastapi import UploadFile
from typing import Annotated
from src.user.helper import save_file

router = APIRouter()


@router.post("/register", tags=["user"])
async def register(
    username: Annotated[EmailStr, Form(...)],
    password: Annotated[str, Form(...)],
    first_name: Annotated[str, Form(...)],
    last_name: Annotated[str, Form(...)],
    telephone: Annotated[str, Form(...)],
    profile_image: UploadFile,
    address: Annotated[str, Form(...)],
    city: Annotated[str, Form(...)],
    province: Annotated[str, Form(...)],
    country: Annotated[str, Form(...)],
):
    profile_image = save_file(profile_image)
    user: dict = {
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "telephone": telephone,
        "profile_image": profile_image,
        "address": address,
        "city": city,
        "province": province,
        "country": country,
    }
    response = requests.post(
        url=f"{config.THE_API_BASE_URL}/api/register",
        data=user,
        files={"profile_image": open(profile_image, "rb")},
    )
    if response.status_code not in [200, 201]:
        return Response(
            response_code=400,
            status="failed",
            message="User not created",
            data=None,
        )
    jwt = create_jwt(user["username"], user["password"])
    user.pop("password")
    user.update("JWT")
    return Response(
        response_code=201,
        status="success",
        message="User created",
        data=user,
        headers={"Authorization": f"TSTMY {jwt}"},
    )
