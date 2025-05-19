


from user.domain.models import User
from user.domain.repositories import UserRepository


class CreateUser:
    
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository
    
    def execute(self, user: User) -> None:
        self._user_repository.create(user)