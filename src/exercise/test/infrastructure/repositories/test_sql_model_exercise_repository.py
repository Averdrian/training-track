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
            
    def test_get_all_exercises_from_database(self) -> None:
        repo = SQLModelExerciseRepository()
        
        with Session(psql_engine) as session:
            session.add(ExerciseModel(
                name="Name1"
            ))
            session.add(ExerciseModel(
                name="Name2"
            ))
            session.commit()
            
        exercises = repo.all()
        assert len(exercises) == 2
        
        with Session(psql_engine) as session:
            session.delete(exercises[0])
            session.delete(exercises[1])
            session.commit()
        
            