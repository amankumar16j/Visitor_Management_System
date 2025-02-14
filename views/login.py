import streamlit as st
from models.user import UserManager

def login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    user_manager = UserManager()

    if st.button("Login"):
        role = user_manager.authenticate_user(username, password)
        if role:
            st.session_state.authenticated = True
            st.session_state.role = role
            st.session_state.username = username
            st.success(f"Logged in as {role}")
            # st.experimental_rerun()
        else:
            st.error("Invalid username or password")
