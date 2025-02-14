import streamlit as st
from models.visitor import VisitorManagement
from functions.qr_generator import generate_qr

def approval_portal():
    st.title("Host Approval Portal")
    visitor_manager = VisitorManagement()
    visitors = visitor_manager.get_pending_visitors()

    if visitors:
        for visitor in visitors:
            visitor_id = visitor[0]  # Unique ID for each visitor
            visitor_name = visitor[1]
            purpose = visitor[3]
            host = visitor[4]

            st.write(f"**Visitor_ID:**{visitor_id} | **Visitor:** {visitor_name} | **Purpose:** {purpose} | **Host:** {host}")
            col1, col2 = st.columns(2)
            
            if col1.button(f"Approve {visitor_name}", key=f"approve_{visitor_id}"):
                visitor_manager.update_visitor_status(visitor_id, "Approved")
                # generate_qr(visitor_id)  # Generate QR code
                st.experimental_rerun()

            if col2.button(f"Reject {visitor_name}", key=f"reject_{visitor_id}"):
                visitor_manager.update_visitor_status(visitor_id, "Rejected")
                st.experimental_rerun()
    else:
        st.info("No pending approvals.")
