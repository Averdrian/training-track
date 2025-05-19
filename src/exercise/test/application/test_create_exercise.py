import pytest
from exercise.application.create_exercise import CreateExercise, CreateExerciseCommand
from exercise.domain.exceptions import NameIsEmpty
from exercise.domain.models import Exercise
from exercise.domain.repositories import ExercicesRepository


class FakeExerciseRepository(ExercicesRepository):
    def __init__(self):
        self._exercises = []

    def save(self, exercise : Exercise):
        self._exercises.append(exercise)
        
    def all(self) -> list[Exercise]:
        return self._exercises

class TestCreateExercise:
    def test_creates_exercise(self) -> None:
        exercise_repository = FakeExerciseRepository()
        CreateExercise(exercise_repository).execute(
            CreateExerciseCommand(
                exercise_name="Example_Exercise"
            )
        )
        
        exercises = exercise_repository.all()
        assert len(exercises) == 1
        assert exercises[0].name() == "Example_Exercise"
        
    
    def test_raise_exception_when_name_is_empty(self) -> None:
        exercise_repository = FakeExerciseRepository()
        
        with pytest.raises(NameIsEmpty):
            CreateExercise(exercise_repository).execute(
                CreateExerciseCommand(
                    exercise_name=""
                )
            )
        
        exercices = exercise_repository.all()
        assert len(exercices) == 0