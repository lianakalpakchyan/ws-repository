import sqlite3 as sq
from contextlib import contextmanager


class SQLiteConnection:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self._conn = sq.connect(db_name)
        self._conn.row_factory = sq.Row
        self._create_tables()

    @contextmanager
    def _get_cursor(self):
        try:
            cursor = self._conn.cursor()
            yield cursor
            self._conn.commit()
        except Exception:
            self._conn.rollback()
            raise

    def _create_tables(self):
        with self._get_cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    age INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def close(self):
        self._conn.close()