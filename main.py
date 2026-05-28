from repos.sqlite import SQLiteRepository
from schemas.users import User
from services.users import UserService


if __name__ == "__main__":
    sql_repo = SQLiteRepository()
    user_service = UserService(sql_repo)
    user1 = User("Alice", "alice@example.com", 30)
    user_service.register(user1)
    print(user_service.find_by_email("alice@example.com"))
