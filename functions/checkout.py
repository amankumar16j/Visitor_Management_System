import streamlit as st
from models.visitor import VisitorManagement
from datetime import datetime

def check_out_visitor():
    name=st.text_input("Full Name")
    visitor_manager=VisitorManagement()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if st.button("Check Out"):
        row_count=visitor_manager.check_out_visitor(name,current_time)
        if row_count > 0:
            st.success(f"{name} checked out at {current_time}")
        else:
            st.warning(f"No visitor found with the name: {name}")