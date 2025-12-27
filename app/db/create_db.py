import sqlite3 as db, os
BASE_DIR = os.path.dirname(__file__)          # folder containing this script
db_path  = os.path.join(BASE_DIR, 'database.db')

with db.connect(db_path) as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            username      TEXT NOT NULL,
            phonenumber   TEXT NOT NULL
        )
    ''')