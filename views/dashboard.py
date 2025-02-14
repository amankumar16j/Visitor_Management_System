import streamlit as st

def dashboard():
    st.subheader(f"Welcome, {st.session_state.username}!")

    if st.session_state.role == "Security":
        st.write("You have security privileges.")
    elif st.session_state.role == "Host":
        st.write("You have host privileges.")
