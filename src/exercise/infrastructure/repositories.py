from sqlmodel import Field, SQLModel, Session, select
from exercise.domain.models import Exercise
from exercise.domain.repositories import ExercicesRepository
from main import psql_engine


class ExerciseModel(SQLModel, table=True):
    __tablename__ = "exercises"
    id: int | None = Field(default=None, primary_key=True)
    name: str

SQLModel.metadata.create_all(psql_engine)

class SQLModelExerciseRepository(ExercicesRepository):
    def all(self) -> list[Exercise]:
        with Session(psql_engine) as session:
            statement = select(ExerciseModel)
            exercise_models = session.exec(statement).all()
        return [
            Exercise(exercise_name=exercise_model.name)
            for exercise_model in exercise_models
        ]
            
    
    def save(self, exercise: Exercise) -> None:
        exercise_model = ExerciseModel(
            name=exercise.name()
        )
        with Session(psql_engine) as session:
            session.add(exercise_model)
            session.commit()