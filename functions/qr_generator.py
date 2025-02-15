import qrcode
import os
from models.visitor import VisitorManagement
import smtplib
from email.message import EmailMessage
from functions.generate_identity_card import id_generator 
from io import BytesIO

def send_QR_to_visitor(visitor_id,visitor_name, contact, purpose, photo_path,qr_path,host_name,company):
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



def generate_qr(visitor_id):
    visitor_manager=VisitorManagement()
    data=visitor_manager.get_visitor_data(visitor_id)
    QR_PATH = "qr_codes"
    if not os.path.exists(QR_PATH):
        os.makedirs(QR_PATH)
    qr = qrcode.make(f"Visitor ID: {visitor_id}")
    qr_path = f"{QR_PATH}/visitor_{visitor_id}.png"
    qr.save(qr_path)
    visitor_manager.update_QR_path(qr_path,visitor_id)
    visitor_name=data[1]
    visitor_contact=data[2]
    visitor_purpose=data[3]
    visitor_host=data[4]
    visitor_photo=data[9]
    company_name=data[5]
    send_QR_to_visitor(visitor_id,visitor_name,visitor_contact,visitor_purpose,visitor_photo,qr_path,visitor_host,company_name)
    if visitor_photo and qr_path:
        id_card_image = id_generator(visitor_name, visitor_id, visitor_host, company_name, visitor_photo, qr_path)

        # Convert PIL image to bytes
        img_bytes = BytesIO()
        id_card_image.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        
        return img_bytes.getvalue()
    
    return None
