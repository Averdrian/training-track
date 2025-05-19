import bcrypt



from user.domain.value_objects import UserEmail, UserName, UserPassword


class User:
    
    def __init__(self, name: str, email: str, password: bytes) -> None:
        self._name = name
        self._email = email
        self._password = password
    
    @classmethod
    def create(cls, username: UserName, email: UserEmail, password: UserPassword) -> None:
        salt = bcrypt.gensalt(rounds=13)
        encrypted_password = bcrypt.hashpw(password, salt)
        return cls(username, email, encrypted_password)


    def name(self) -> None:
        return self._name
    
    def email(self) -> None:
        return self._email
    
    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password, self._password)
    