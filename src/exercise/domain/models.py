from exercise.domain.value_objects import ExerciseName


class Exercise:
    
    def __init__(self, exercise_name: str):
        self._exercise_name = exercise_name
    
    @classmethod
    def create(cls, exercise_name: ExerciseName) -> "Exercise":
        return cls(exercise_name)
        
    def name(self) -> str:
        return self._exercise_name