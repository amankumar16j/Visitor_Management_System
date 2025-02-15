import streamlit as st
from models.user import UserManager

def signup():
    st.subheader("Sign Up")

    new_username = "Admin"
    new_password = "Admin@1234"
    confirm_password = "Admin@1234"

    user_manager = UserManager()
    result = user_manager.add_user(new_username, new_password, "Admin",0)  # Default role
    

signup()
