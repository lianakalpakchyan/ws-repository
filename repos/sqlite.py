import sqlite3 as sq

from db.connection import SQLiteConnection
from exceptions import DuplicateEmailError
from schemas.users import User


class SQLiteRepository(SQLiteConnection):
    def save(self, user: User) -> User:
        try:
            with self._get_cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                    (user.name, user.email, user.age)
                )
                return user
        except sq.IntegrityError:
            raise DuplicateEmailError(f"User with '{user.email}' email already exists")

    def find_by_email(self, email: str):
        with self._get_cursor() as cursor:
            cursor.execute(
                "SELECT name, email, age, id FROM users WHERE email = ?",
                (email,)
            )
            user = cursor.fetchone()
            return User(**user) if user else None
