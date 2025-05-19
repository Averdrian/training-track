from abc import ABC, abstractmethod
from exercise.domain.models import Exercise


class ExercicesRepository(ABC):
    @abstractmethod
    def all(self) -> list[Exercise]: ...
    
    @abstractmethod
    def save(self, exercise: Exercise) -> None: ...