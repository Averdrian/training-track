
from abc import ABC, abstractmethod

from user.domain.models import User


class UserRepository(ABC):
    
    @abstractmethod
    def create(self, user: User) -> None: ...
    
    @abstractmethod
    def all(self) -> list[User]: ... 