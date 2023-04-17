from src.auth.service import jwt_required
from fastapi import APIRouter, Depends
from src.response import Response
import requests
from src.dependencies import config
from typing import Optional

router = APIRouter()


@router.get("/", tags=["article"], dependencies=[Depends(jwt_required)])
async def get_articles(limit: Optional[int], offset: Optional[int]):
    response = requests.get(
        url=f"{config.THE_API_BASE_URL}/api/article?limit={limit}&offset={offset}"
    )
    if response.status_code == 200:
        return Response(
            response_code=200,
            status="success",
            message="Articles retrieved",
            data=response.json(),
        )
    else:
        return Response(
            response_code=400,
            status="failed",
            message="Articles not retrieved",
            data=None,
        )


@router.get("/{id}", tags=["article"], dependencies=[Depends(jwt_required)])
async def get_article_by_id(id: int):
    response = requests.get(url=f"{config.THE_API_BASE_URL}/api/article/{id}")
    if response.status_code == 200:
        return Response(
            response_code=200,
            status="success",
            message="Article retrieved",
            data=response.json(),
        )
    else:
        return Response(
            response_code=400,
            status="failed",
            message="Article not retrieved",
            data=None,
        )
