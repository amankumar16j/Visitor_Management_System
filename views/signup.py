import streamlit as st
from models.user import UserManager

def signup():
    st.subheader("Sign Up")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    role = st.selectbox("Select Role", ["Admin", "Security", "Host"],index=1)  
    if role=="Security":
        pre_approval_limit=0
    if role=="Host":
        pre_approval_limit = st.number_input(
            "Enter Pre-Approval Limit", 
            min_value=0, 
            max_value=10, 
            step=1, 
            value=0
        )
    user_manager = UserManager()

    if st.button("Sign Up"):
        if new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            result = user_manager.add_user(new_username, new_password, role,pre_approval_limit)  # Default role
            st.success(result)
