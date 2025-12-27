from importlib.resources import path
import os
import sqlite3 as db
def register_user(input_dict):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SQLPATH = os.path.join(BASE_DIR, 'database.db')

    conn = db.connect(SQLPATH)
    conn.execute('INSERT INTO users (username, phonenumber) VALUES (?, ?)', (input_dict['username'], input_dict['phonenumber']))
    conn.commit()
    conn.close()
    
def find_user_phone(username: str):
    print('LOOKING FOR:', repr(username))
    """Return phone number or None if username does not exist."""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path  = os.path.join(BASE_DIR, 'database.db')
    with db.connect(db_path) as conn:
        cur = conn.execute(
            'SELECT phonenumber FROM users WHERE username = ?', (username,)
        )
        row = cur.fetchone()
        return row[0] if row else None