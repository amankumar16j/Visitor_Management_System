import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY, 
                        hashed_password TEXT,
                        password TEXT,
                        role TEXT,
                        pre_approval_limit INTEGER
                    )''')  # Removed trailing comma & added INTEGER
    conn.commit()
    conn.close()
