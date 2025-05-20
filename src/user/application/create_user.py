


from dataclasses import dataclass
from user.domain.repositories import UserRepository

@dataclass
class CreateUserCommand:
   username : str
   email : str
   password : str 


class CreateUser:
    
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository
    
    def execute(self, user: CreateUserCommand) -> None:
        self._user_repository.create(user)