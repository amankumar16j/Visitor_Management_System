import streamlit as st
from models.user import UserManager

def delete():
    st.subheader("Delete User")

    delete_username = st.text_input("Delete Username")
    confirmation=st.text_input("To Confirm Deletion Write <Delete user_name> ")
    
    user_manager = UserManager()

    if st.button("Delete User"):
        if "Delete "+ delete_username != confirmation:
            st.warning("User didn't deleted")
        else:
            result = user_manager.delete_user(delete_username)  # Default role
            st.success(result)