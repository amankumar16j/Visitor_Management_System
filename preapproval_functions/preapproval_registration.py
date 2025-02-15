import streamlit as st
from models.preapproval import PreapprovalManagement
from PIL import Image
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage
from functions.generate_visitor_id import generate_visitor_id
import qrcode
from io import BytesIO
from functions.generate_identity_card import id_generator 
from models.user import UserManager

# Function to send email using App Password
def send_email_to_visitor(visitor_id,visitor_name, contact, purpose, photo_path,qr_path,host_name,company):
    sender_email = "sam1sepagrawal@gmail.com"  # Replace with your Gmail
    app_password = "gtac gdts ypuz zlib"  # Replace with the generated App Password
    host_email="aman17jilm@gmail.com"
    msg = EmailMessage()
    msg['Subject'] = f"Visitor Registration Confirmation: {visitor_name}"
    msg['From'] = sender_email
    msg['To'] = contact  # Ensure you're sending it to the visitor

    msg.set_content(f"""
    Hello {visitor_name},

    Welcome !!  

    Your visit has been successfully registered. Please find your QR code attached, which you will need for check-in at the reception.  

    ### **Visitor Details:**  
    - **Name:** {visitor_name}  
    - **Visitor ID:** {visitor_id}  
    - **Contact:** {contact}  
    - **Purpose of Visit:** {purpose}  
    - **Meeting With:** {host_name} 

    📌 **Instructions:**  
    - Please present this email and your QR code at the reception upon arrival.  
    - If you have any questions, feel free to contact us at {host_email} or visit our reception desk.  

    We look forward to welcoming you!  

    Best regards,  
    **Security Team** 
    """)
    if photo_path and qr_path:
        id_card_image = id_generator(visitor_name, visitor_id, host_name, company, photo_path, qr_path)
        # st.image(id_card_image, caption="Generated ID Card", use_column_width=False)


    # Attach the visitor's photo
    if id_card_image:
        img_bytes = BytesIO()
        id_card_image.save(img_bytes, format="PNG")  # Convert PIL image to bytes
        img_bytes.seek(0)
        msg.add_attachment(img_bytes.getvalue(), maintype='image', subtype='png', filename="Visitor_ID_Card.png")
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
def preapproval_registration():
    st.title("Pre-Approval Registration")
    preapproval_manager = PreapprovalManagement()
    user_manager=UserManager()
    
    current_user=st.session_state.username
    current_date = datetime.now().strftime("%Y-%m-%d")
    preapproval_limit=user_manager.get_preapproval_limit(current_user)
    current_preapproval_count=preapproval_manager.count_preapprovals_today(current_user,current_date)
    
    if current_preapproval_count<preapproval_limit:
        name = st.text_input("Full Name")
        contact = st.text_input("Contact (Phone/Email)")
        purpose = st.text_input("Purpose of Visit")
        host = current_user
        company = st.text_input("Company (if applicable)")
        photo = st.file_uploader("Upload Photo", type=["jpg", "png", "jpeg"])
        government_id_proof = st.file_uploader("Upload Government ID Proof", type=["jpg", "png", "jpeg"])
        last_checkin_time=datetime.now().strftime('%Y-%m-%d') + ' 5:30:00'
        if st.button("Register Pre-Approval"):
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

                preapproval_manager.insert_visitor(visitor_id,name, contact, purpose, host, company, photo_path, government_id_proof_path,last_checkin_time)
                
                QR_PATH = "qr_codes"
                if not os.path.exists(QR_PATH):
                    os.makedirs(QR_PATH)
                qr = qrcode.make(f"Visitor ID: {visitor_id}")
                qr_path = f"{QR_PATH}/visitor_{visitor_id}.png"
                qr.save(qr_path)
                preapproval_manager.update_QR_path(qr_path,visitor_id)
                
                email_sent = send_email_to_visitor(visitor_id,name, contact, purpose,photo_path,qr_path,host,company)

                if "success_message" not in st.session_state:
                    st.session_state.success_message = None
                    
                if email_sent:
                    st.session_state.success_message = f"Visitor {name} with VisitorID {visitor_id} registered! Email sent."
                else:
                    st.warning("Visitor registered, but failed to send email.")
                    
                if st.session_state.success_message:
                    st.success(st.session_state.success_message)
                
                return visitor_id
    else:
        st.warning("You have exhausted your Pre-Approval Limit For Today")
