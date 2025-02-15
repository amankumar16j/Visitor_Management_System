import sqlite3

def init_db():
    conn = sqlite3.connect("pre_approval.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pre_approval (
            id TEXT PRIMARY KEY,
            name TEXT,
            contact TEXT,
            purpose TEXT,
            host TEXT,
            company TEXT,
            last_checkin_time TIMESTAMP,
            photo_path TEXT,
            government_id_proof TEXT,
            qr_path TEXT
        )        
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()
