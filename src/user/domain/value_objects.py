
from dataclasses import dataclass
import validators

from user.domain.exceptions import InvalidEmail, InvalidPassword, InvalidUsername


@dataclass(frozen=True, kw_only=True)
class UserName:
    value : str
    
    def __post_init__(self) -> None:
        if self.value == "":
            raise InvalidUsername
        
        
@dataclass(frozen=True, kw_only=True)
class UserEmail:
    value: str
    
    def __post_init__(self) -> None:
        if not validators.email(self.value):
            raise InvalidEmail
        
@dataclass(frozen=True, kw_only=True)
class UserPassword:
    value: str
    
    def __post_init__(self) -> None:
        if self.value == "":
            raise InvalidPassword