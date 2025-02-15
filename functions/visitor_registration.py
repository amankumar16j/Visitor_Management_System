import streamlit as st
from models.visitor import VisitorManagement
from PIL import Image
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage
from functions.generate_visitor_id import generate_visitor_id

# Function to send email using App Password
def send_email_to_host(visitor_id,visitor_name, contact, purpose, company, photo_path, government_id_proof_path):
    sender_email = "sam1sepagrawal@gmail.com"  # Replace with your Gmail
    app_password = "gtac gdts ypuz zlib"  # Replace with the generated App Password
    host_email="aman17jilm@gmail.com"
    msg = EmailMessage()
    msg['Subject'] = f"Visitor Approval Request: {visitor_name}"
    msg['From'] = sender_email
    msg['To'] = host_email
    msg.set_content(f"""
                        Hello,

                        A visitor has registered and is awaiting your approval.

                        **Visitor Details:**
                        - **Name:** {visitor_name}
                        - **Visitor ID:** {visitor_id}
                        - **Contact:** {contact}
                        - **Purpose of Visit:** {purpose}
                        - **Company:** {company}

                        Please review and approve the visitor.

                        Best regards,  
                        Security Team
                    """)

    # Attach the visitor's photo
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as f:
            img_data = f.read()
            msg.add_attachment(img_data, maintype='image', subtype='jpeg', filename=os.path.basename(photo_path))

    #Attach the visitor's government
    if os.path.exists(government_id_proof_path):
        with open(government_id_proof_path, 'rb') as f:
            img_data2 = f.read()
            msg.add_attachment(img_data2, maintype='image', subtype='jpeg', filename=os.path.basename(government_id_proof_path))

    # Send email using SMTP with App Password
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

# Streamlit UI for Visitor Registration
def visitor_registration():
    st.title("Visitor Registration")

    current_datetime = datetime.now()
    checkin_time=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    visitor_manager = VisitorManagement() 
    name = st.text_input("Full Name")
    contact = st.text_input("Contact (Phone/Email)")
    purpose = st.text_input("Purpose of Visit")
    host = st.text_input("Host Employee Name")
    company = st.text_input("Company (if applicable)")
    photo = st.file_uploader("Upload Photo", type=["jpg", "png", "jpeg"])
    government_id_proof = st.file_uploader("Upload Government ID Proof", type=["jpg", "png", "jpeg"])
    # visitor_id=""
    if st.button("Register Visitor"):
        if not (name and contact and purpose and host and photo and government_id_proof):
            st.error("All fields are required, including a photo.")
        else:
            visitor_id=generate_visitor_id(name)
            
            photo_path = f"photos/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            os.makedirs("photos", exist_ok=True)
            image = Image.open(photo)
            image.save(photo_path)
            
            government_id_proof_path = f"government_id_proof/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            os.makedirs("government_id_proof", exist_ok=True)
            image2 = Image.open(government_id_proof)
            image2.save(government_id_proof_path)

            visitor_manager.insert_visitor(visitor_id,name, contact, purpose, host, company, photo_path, government_id_proof_path,checkin_time)
            email_sent = send_email_to_host(visitor_id,name, contact, purpose, company, photo_path,government_id_proof_path)

            if "success_message" not in st.session_state:
                st.session_state.success_message = None
                
            if email_sent:
                st.session_state.success_message = f"Visitor {name} with VisitorID {visitor_id} registered! Email sent to the host for approval."
            else:
                st.warning("Visitor registered, but failed to send email.")
                
            if st.session_state.success_message:
                st.success(st.session_state.success_message)
            
            return visitor_id

