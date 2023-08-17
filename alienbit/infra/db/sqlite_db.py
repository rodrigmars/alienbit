import sqlite3
from typing import Callable

def connection_db(local_db:str) -> Callable[[], sqlite3.Connection]: 

    def create_connection() -> sqlite3.Connection:
        return sqlite3.connect(local_db)

    return create_connection