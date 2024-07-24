from fastapi import HTTPException, status
from app.common.custom_errors import (
    CustomError,
    BadRequestError,
    SuccessError,
    InternalServerError,
)


def handle_custom_error(error: CustomError):
    if isinstance(error, BadRequestError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": error.code, "message": error.message},
        )
    elif isinstance(error, InternalServerError):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"code": error.code, "message": error.message},
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail={"code": error.code, "message": error.message},
        )
