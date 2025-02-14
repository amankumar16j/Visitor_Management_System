import streamlit as st
from models.visitor import VisitorManagement
from PIL import Image
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Function to send email using App Password
def send_email_to_host(visitor_name, contact, purpose, company, photo_path):
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

    visitor_manager = VisitorManagement()  
    name = st.text_input("Full Name")
    contact = st.text_input("Contact (Phone/Email)")
    purpose = st.text_input("Purpose of Visit")
    host = st.text_input("Host Employee Name")
    # host_email = st.text_input("Host Email")  # Input for host email
    company = st.text_input("Company (if applicable)")
    photo = st.file_uploader("Upload Photo", type=["jpg", "png", "jpeg"])

    if st.button("Register Visitor"):
        if not (name and contact and purpose and host and photo):
            st.error("All fields are required, including a photo.")
        else:
            photo_path = f"photos/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            os.makedirs("photos", exist_ok=True)
            image = Image.open(photo)
            image.save(photo_path)

            visitor_manager.insert_visitor(name, contact, purpose, host, company, photo_path)
            email_sent = send_email_to_host(name, contact, purpose, company, photo_path)

            if email_sent:
                st.success("Visitor registered! Email sent to the host for approval.")
            else:
                st.warning("Visitor registered, but failed to send email.")

