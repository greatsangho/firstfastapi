from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        """
        Find a user by email
        검색한 유저가 없을 경우 422 에러를 발생시킨다
        """
        raise NotImplementedError