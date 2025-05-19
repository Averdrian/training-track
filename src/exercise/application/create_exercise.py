
from dataclasses import dataclass
from exercise.domain.models import Exercise
from exercise.domain.repositories import ExercicesRepository
from exercise.domain.value_objects import ExerciseName

@dataclass
class CreateExerciseCommand:
    exercise_name : str


class CreateExercise:
    
    def __init__(self, exerciseRepository: ExercicesRepository):
        self._exercises_repository = exerciseRepository
    
    def execute(self, command: CreateExerciseCommand) -> None:
        exercise_name = ExerciseName(value=command.exercise_name)
        exercise = Exercise.create(exercise_name=exercise_name)
        self._exercises_repository.save(exercise)