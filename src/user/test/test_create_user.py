

from user.application.create_user import CreateUser
from user.domain.models import User
from user.domain.repositories import UserRepository


class FakeUserRepository(UserRepository):
    
    def __init__(self):
        self._users = []
        
    def create(self, user: User) -> None:
        self._users.append(user)
        
    def all(self) -> list[User]:
        return self._users


class TestCreateUser:    
    
    def test_creates_user(self) -> None:
        user_repository = FakeUserRepository()
        
        CreateUser(user_repository).execute(
            User()
        )
        
        assert len(user_repository.all()) == 1
        