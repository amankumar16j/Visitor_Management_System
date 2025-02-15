import sqlite3
import streamlit as st
from models.user import UserManager
import pandas as pd

def admin_dashboard():
   
    st.subheader("Admin Panel - List of All the users present")
    user_manager = UserManager()
    st.subheader("Existing Users")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username , role  FROM users")
    users = cursor.fetchall()
    conn.close()
    
    df = pd.DataFrame(users, columns=["Username", "Role"])

    st.table(df)
    # st.table(users)
