
from exercise.domain.repositories import ExercicesRepository


class CreateExercise:
    
    def __init__(self, exerciseRepository: ExercicesRepository):
        self._exercises_repository = exerciseRepository
    
    def execute(self) -> None:
        pass