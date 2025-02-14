import sqlite3

def init_db():
    conn = sqlite3.connect("visitor_management.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            purpose TEXT,
            host TEXT,
            company TEXT,
            checkin_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            checkout_time TIMESTAMP,
            status TEXT DEFAULT 'Pending',
            photo_path TEXT,
            qr_path TEXT
        )
    ''')
    conn.commit()
    conn.close()