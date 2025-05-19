
from dataclasses import dataclass
from exercise.domain.models import Exercise
from exercise.domain.repositories import ExercicesRepository

@dataclass
class CreateExerciseCommand:
    exercise_name : str


class CreateExercise:
    
    def __init__(self, exerciseRepository: ExercicesRepository):
        self._exercises_repository = exerciseRepository
    
    def execute(self, command: CreateExerciseCommand) -> None:
        self._exercises_repository.save(Exercise())