from protocols.repo import Repository
from schemas.users import User


class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository

    def register(self, user: User) -> None:
        self.repository.save(user.__dict__)

    def find_by_email(self, email: str) -> User | None:
        user_data = self.repository.find_by_email(email)
        return User(**user_data) if user_data else None
