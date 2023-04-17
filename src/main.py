from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.user.route import router as user_router
from src.article.route import router as article_router


app = FastAPI(title="The Proxy API", description="a Proxy API for The API")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(article_router, prefix="/article", tags=["article"])
