import pytest
from sqlmodel import Session, select
from exercise.domain.models import Exercise
from exercise.infrastructure.repositories import SQLModelExerciseRepository, psql_engine, ExerciseModel


class TestSQLModelExerciseRepository:

    def test_saves_exercise_to_database(self) -> None:
        repo = SQLModelExerciseRepository()
        
        repo.save(Exercise(
            exercise_name="TestExercise"
        ))
        
        with Session(psql_engine) as session:
            statement = select(ExerciseModel).where(ExerciseModel.name == "TestExercise")
            
            exercise = session.exec(statement).first()
            assert exercise is not None
            
            session.delete(exercise)
            session.commit()