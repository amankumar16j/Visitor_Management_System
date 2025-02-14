import sqlite3
from db.visitordatabase import init_db
# DB_PATH = "visitor_management.db"

class VisitorManagement:
    def __init__(self,db_path="visitor_management.db"):
        self.db_path=db_path
        init_db()

    def insert_visitor(self,name, contact, purpose, host, company,photo_path):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO visitors (name, contact, purpose, host, company, photo_path) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, contact, purpose, host, company, photo_path))
        conn.commit()
        conn.close()

    def get_pending_visitors(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM visitors WHERE status = 'Pending'")
        visitors = cursor.fetchall()
        conn.close()
        return visitors

    def update_visitor_status(self,visitor_id, status):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE visitors SET status = ? WHERE id = ?", (status, visitor_id))
        conn.commit()
        conn.close()
    
    def check_visitor_status(self,visitor_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM visitors WHERE name=?", (visitor_name,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None  # Return status if found, else None

    def check_out_visitor(self,visitor_name,current_time):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE visitors SET checkout_time = ? WHERE name = ?", (current_time, visitor_name))
        conn.commit() 
        row_count = cursor.rowcount
        # result = cursor.fetchone()
        conn.close()
        return row_count
    
    def update_QR_path(self,qr_path,visitor_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE visitors SET qr_path = ? WHERE name = ?", (qr_path, visitor_name))
        conn.commit() 
        row_count = cursor.rowcount
        # result = cursor.fetchone()
        conn.close()
        return row_count
    
    def get_visitor_data(self,visitor_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM visitors WHERE name=?", (visitor_name,))
        result = cursor.fetchone()
        conn.close()
        return result if result else None  # Return status if found, else None
        
        
        