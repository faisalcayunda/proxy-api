from fastapi import HTTPException, Request
from src.dependencies import config
import requests


def jwt_required(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token not found")
    token = token.split(" ")[1]
    response = requests.post(
        f"{config.THE_API_BASE_URL}/api/api/token/refresh/",
        data={"refresh": token},
    )
    if response.status_code == 200:
        return True
    else:
        raise HTTPException(status_code=401, detail="Invalid token")


def create_jwt(username, password):
    response = requests.post(
        f"{config.THE_API_BASE_URL}/api/token/",
        data={"username": username, "password": password},
    )
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
