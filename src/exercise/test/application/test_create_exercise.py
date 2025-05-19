from exercise.application.create_exercise import CreateExercise
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
        CreateExercise(exercise_repository).execute(Exercise())
        
        assert len(exercise_repository.all()) == 1
        
        