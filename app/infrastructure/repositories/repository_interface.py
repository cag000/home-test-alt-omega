from typing import TypeVar, Generic, List, Optional
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepositoryInterface(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def get(self, id: int) -> Optional[ModelType]:
        raise NotImplementedError

    def get_all(self, skip: int = 0, limit: int = 10) -> List[ModelType]:
        raise NotImplementedError

    def create(self, obj_in: CreateSchemaType) -> ModelType:
        raise NotImplementedError

    def update(self, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        raise NotImplementedError

    def delete(self, id: int) -> None:
        raise NotImplementedError
