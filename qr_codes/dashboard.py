import streamlit as st
import sqlite3
import streamlit as st
from models.user import UserManager
import pandas as pd

def dashboard():
    
    st.subheader(f"Welcome, {st.session_state.username}!")
    if st.session_state.role == "Security":
        st.write("You have security privileges.")
        st.subheader("List of All the visitors registered")
        user_manager = UserManager()
        conn = sqlite3.connect('visitor_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, checkin_time, host, contact, status FROM visitors ORDER BY checkin_time DESC LIMIT 10;")
        latest_visitors = cursor.fetchall()
        conn.close()

        df = pd.DataFrame(latest_visitors, columns=["Visitor_ID","Visitor_name", "Checkin Time", "Host", "Contact", "Status"])
        st.table(df)
    elif st.session_state.role == "Host":
        
        if "username" not in st.session_state:
            st.error("No username found in session. Please log in first.")
        else:
            username = st.session_state.username
            st.write("You have host privileges.")
            st.subheader(f"List of All Visitors Registered for {username}")

            try:
                conn = sqlite3.connect('visitor_management.db')
                cursor = conn.cursor()

                # Fetch latest 10 visitors for the host
                cursor.execute(
                    "SELECT id, name, checkin_time, contact, status FROM visitors WHERE host = ? ORDER BY checkin_time DESC LIMIT 10",
                    (username,)
                )
                latest_visitors = cursor.fetchall()
                conn.close()

                # Check if data is available
                if latest_visitors:
                    df = pd.DataFrame(latest_visitors, columns=["Visitor_ID", "Visitor_name", "Checkin Time", "Contact", "Status"])
                    st.table(df)
                else:
                    st.info("No visitors registered under your name.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        
