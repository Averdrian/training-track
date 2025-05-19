from exercise.domain.models import Exercise
from exercise.domain.repositories import ExercicesRepository


class PostgreSQLExerciseRepository(ExercicesRepository):
    def all(self) -> list[Exercise]:
        return None
    
    def save(self, exercise: Exercise) -> None:
        return None