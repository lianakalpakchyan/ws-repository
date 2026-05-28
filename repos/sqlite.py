import sqlite3 as sq

from db.connection import SQLiteConnection
from exceptions import DuplicateEmailError
from protocols.repo import Repository


class SQLiteRepository(Repository, SQLiteConnection):
    def save(self, data: dict) -> None:
        try:
            with self._get_cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                    (data["name"], data["email"], data["age"])
                )
        except sq.IntegrityError:
            raise DuplicateEmailError(f"User with '{data["email"]}' email already exists")

    def find_by_email(self, email: str) -> dict | None:
        with self._get_cursor() as cursor:
            cursor.execute(
                "SELECT name, email, age, id FROM users WHERE email = ?",
                (email,)
            )
            data = cursor.fetchone()
            return  {"name": data["name"], "email": data["email"], "age": data["age"]} if data else None
