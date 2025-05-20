
from user.domain.models import User
from user.domain.repositories import UserRepository


class SQLModelUserRepository(UserRepository):
    
    def create(self, user: User) -> None:
        pass
    
    def all(self) -> list[User]:
        pass