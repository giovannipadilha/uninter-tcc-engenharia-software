import sqlite3

DATABASE_NAME = "products.db"


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(DATABASE_NAME, check_same_thread=False)

    _create_table_if_not_exists(connection)
    
    return connection


def _create_table_if_not_exists(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
        """
    )

    connection.commit()
