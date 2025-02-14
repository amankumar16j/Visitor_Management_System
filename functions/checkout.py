import streamlit as st
from models.visitor import VisitorManagement
from datetime import datetime

def check_out_visitor():
    visitor_id=st.text_input("Visitor_ID")
    visitor_manager=VisitorManagement()
    data=visitor_manager.get_visitor_data(visitor_id)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if st.button("Check Out"):
        row_count=visitor_manager.check_out_visitor(visitor_id,current_time)
        if row_count > 0:
            st.success(f"{data[1]} checked out at {current_time}")
        else:
            st.warning(f"No visitor found with the ID: {visitor_id}")