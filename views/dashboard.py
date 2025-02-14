import streamlit as st
import sqlite3
import streamlit as st
from models.user import UserManager
import pandas as pd

def dashboard():
    st.subheader(f"Welcome, {st.session_state.username}!")
    if st.session_state.role == "Security":
        st.write("You have security privileges.")
        st.subheader("List of All the users registered")
        user_manager = UserManager()
        conn = sqlite3.connect('visitor_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, checkin_time, host, contact, status FROM visitors ORDER BY checkin_time DESC LIMIT 10;")
        latest_visitors = cursor.fetchall()
        conn.close()

        df = pd.DataFrame(latest_visitors, columns=["Visitor_ID","Visitor_name", "Checkin Time", "Host", "Contact", "Status"])
        st.table(df)
    elif st.session_state.role == "Host":
        st.write("You have host privileges.")
        
