from typing import Any
from fastapi.responses import JSONResponse


class Response:
    def __init__(self, response_code, status, message, data, headers=None):
        self.response_code = response_code
        self.status = status
        self.message = message
        self.data = data
        self.headers = headers

    def __call__(self, *args: Any, **kwds: Any) -> dict:
        content: Any = {
            "status": self.status,
            "message": self.message,
            "data": self.data,
        }
        return JSONResponse(
            content=content,
            status_code=self.response_code,
            media_type="application/json",
            headers=self.headers,
        )

    def __str__(self) -> str:
        return str(self.__dict__)
