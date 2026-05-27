from typing import Protocol

from exceptions import DuplicateEmailError
from repos.sqlite import SQLiteRepository
from schemas.users import User

class Repository(Protocol):
    def save(self, user: dict) -> None: ...
    def find_by_email(self, email: str) -> dict: ...


class UserService:
    def __init__(self, repository: SQLiteRepository):
        self.repository = repository

    def register(self, user: User) -> None:
        try:
            self.repository.save(user)
        except DuplicateEmailError:
            print("User already exists")

    def find_by_email(self, email: str) -> User | None:
        return self.repository.find_by_email(email)


if __name__ == "__main__":
    sql_repo = SQLiteRepository()
    user_service = UserService(sql_repo)
    user1 = User("Alice", "alice@example.com", 30)
    user_service.register(user1)
    print(user_service.find_by_email("alice@example.com"))
