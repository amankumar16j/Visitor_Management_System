import sqlite3
from db.pre_approval_database import init_db
from datetime import datetime
# DB_PATH = "visitor_management.db"

class PreapprovalManagement:
    def __init__(self,db_path="pre_approval.db"):
        self.db_path=db_path
        init_db()

    def insert_visitor(self,visitor_id,name, contact, purpose, host, company,photo_path,government_id_proof_path,last_checkin_time):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pre_approval (id,name, contact, purpose, host, company, photo_path, government_id_proof,last_checkin_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (visitor_id, name, contact, purpose, host, company, photo_path,government_id_proof_path,last_checkin_time))
        conn.commit()
        conn.close()
    
    def update_QR_path(self,qr_path,visitor_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE pre_approval SET qr_path = ? WHERE id = ?", (qr_path, visitor_id))
        conn.commit() 
        row_count = cursor.rowcount
        conn.close()
        return row_count
    
    def get_visitor_data(self,visitor_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pre_approval WHERE id=?", (visitor_id,))
        result = cursor.fetchone()
        conn.close()
        return result if result else None  # Return status if found, else None
    
    def delete_preapproval(self,visitor_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pre_approval WHERE id = ?", (visitor_id,))
        conn.commit() 
        row_count = cursor.rowcount
        conn.close()
        return row_count
    
    def count_preapprovals_today(self,host,current_date):
        conn = sqlite3.connect("pre_approval.db")
        cursor = conn.cursor()

        # Query to count preapprovals where only the date part matches today's date
        cursor.execute("""
            SELECT COUNT(*) 
            FROM pre_approval 
            WHERE DATE(last_checkin_time) = ? AND host= ?
        """, (current_date,host))

        count = cursor.fetchone()[0]  # Fetch count result
        conn.close()

        return count

        
        
        
        