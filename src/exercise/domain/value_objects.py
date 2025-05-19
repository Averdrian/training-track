
from dataclasses import dataclass

from exercise.domain.exceptions import NameIsEmpty


@dataclass(frozen=True, kw_only=True)
class ExerciseName:
    value: str
    
    def __post_init__(self) -> None:
        if self.value == "":
            raise NameIsEmpty