import streamlit as st
import sqlite3
from functions.qr_generator import generate_qr
from PIL import Image
from models.visitor import VisitorManagement
import os
from io import BytesIO

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
            
            id_card_data = generate_qr(visitor_id)  # Get ID card as bytes
            
            if id_card_data:  # Check if image data is valid
                st.download_button(
                    label="📥 Download ID Card",
                    data=id_card_data,
                    file_name="Visitor_ID_Card.png",
                    mime="image/png"
                )
                st.image(Image.open(BytesIO(id_card_data)), caption="Generated ID Card", use_column_width=False)
            else:
                st.error("Failed to generate ID card. Please try again.")  
        elif status == "Rejected":
            st.error(f"Visitor {visitor_name} is Rejected ❌")
        elif status:
            st.warning(f"Visitor {visitor_name} is still Waiting for Approval ⏳")
        else:
            st.error("No record found. Please check the name. Or wait until Host Approves you")
