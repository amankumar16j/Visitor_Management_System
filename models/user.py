import sqlite3
from utils.security import hash_password, verify_password
from db.memberdatabase import init_db

class UserManager:
    def __init__(self, db_path='users.db'):
        self.db_path = db_path
        init_db()
    
    def add_user(self, username, password, role):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return "User already exists!"
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                       (username, hashed_password, role))
        conn.commit()
        conn.close()
        return "User created successfully!"

    def authenticate_user(self, username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        if user and verify_password(password, user[0]):
            return user[1]
        return None
    
    def delete_user(self,username):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()
        conn.close()
