import streamlit as st
import sqlite3
from functions.qr_generator import generate_qr
from PIL import Image
from models.visitor import VisitorManagement
import os

def visitor_status(visitor_id):
    st.title("Visitor Status Check")
    visitor_manager=VisitorManagement()
    visitor_id = st.text_input("Enter Visitor ID to Check Status",value=visitor_id)
    
    if st.button("Check Status"):
        status = visitor_manager.check_visitor_status(visitor_id)
        if(visitor_id):
            data=visitor_manager.get_visitor_data(visitor_id)
            visitor_name=data[1]

        if status == "Approved":
            st.success(f"Visitor {visitor_name} is Approved ✅")
            qr_path = generate_qr(visitor_id) # Generate QR for approved visitor
            if os.path.exists(qr_path):
                with open(qr_path, 'rb') as f:
                    img_data = f.read()
            st.image(img_data, caption="Your QR Code", width=200)
        elif status == "Rejected":
            st.error(f"Visitor {visitor_name} is Rejected ❌")
        elif status:
            st.warning(f"Visitor {visitor_name} is still Waiting for Approval ⏳")
        else:
            st.error("No record found. Please check the name. Or wait until Host Approves you")
