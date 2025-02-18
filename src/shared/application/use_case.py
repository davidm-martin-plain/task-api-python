from abc import ABC, abstractmethod
from typing import TypeVar, Generic

UseCaseResponse = TypeVar('UseCaseResponse')

class UseCase(ABC, Generic[UseCaseResponse]):
    @abstractmethod
    def execute(self) -> UseCaseResponse:
        pass