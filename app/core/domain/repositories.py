from typing import List, Optional, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def get(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 10) -> List[T]:
        pass

    @abstractmethod
    async def create(self, entity: T) -> T:
        pass

    @abstractmethod
    async def update(self, id: int, entity: T) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass
