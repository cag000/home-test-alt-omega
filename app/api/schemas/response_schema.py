from pydantic import BaseModel
from typing import Any, List, Optional


class SingleObjectResponse(BaseModel):
    message: str
    data: Optional[Any]


class ListObjectResponse(BaseModel):
    message: str
    data: List[Any]


class SuccessResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    message: str
