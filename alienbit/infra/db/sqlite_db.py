import sqlite3

def connection() -> sqlite3.Connection: 
    return sqlite3.connect(':memory:')