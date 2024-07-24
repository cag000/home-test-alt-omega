from typing import Generic, TypeVar, Type, List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.infrastructure.repositories.repository_interface import BaseRepositoryInterface

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseRepository(
    Generic[ModelType, CreateSchemaType, UpdateSchemaType],
    BaseRepositoryInterface[ModelType, CreateSchemaType, UpdateSchemaType],
):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get(self, id: int) -> Optional[ModelType]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> List[ModelType]:
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db_obj: CreateSchemaType) -> ModelType:
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: ModelType, obj_in: UpdateSchemaType) -> ModelType:
        update_data = obj_in.dict()
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> None:
        obj = self.db.query(self.model).get(id)
        self.db.delete(obj)
        self.db.commit()
