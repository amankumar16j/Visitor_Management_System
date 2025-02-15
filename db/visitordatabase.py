import sqlite3

def init_db():
    conn = sqlite3.connect("visitor_management.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id TEXT PRIMARY KEY,
            name TEXT,
            contact TEXT,
            purpose TEXT,
            host TEXT,
            company TEXT,
            checkin_time TIMESTAMP,
            checkout_time TIMESTAMP,
            status TEXT DEFAULT 'Pending',
            photo_path TEXT,
            government_id_proof TEXT,
            qr_path TEXT
        )
    ''')
    conn.commit()
    conn.close()