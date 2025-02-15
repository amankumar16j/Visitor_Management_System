import streamlit as st
from models.preapproval import PreapprovalManagement
from models.visitor import VisitorManagement
from datetime import datetime


def validate_preapproval():
    
    st.title("Check if Valid Pre-Approval")
    visitor_id = st.text_input("Enter Visitor ID to Check Pre-Approval")
    if st.button("Check Pre-Approval"):
        preapproval_manager=PreapprovalManagement()
        visitor_manager=VisitorManagement()
        data=preapproval_manager.get_visitor_data(visitor_id)
        
        if data:
            visitor_name=data[1]
            visitor_contact=data[2]
            purpose=data[3]
            host=data[4]
            company=data[5]
            last_checkin_time_str=data[6]
            photo_path=data[7]
            government_id_proof_path=data[8]
            qr_path=data[9]
            

            #  Extract only the time component
            last_checkin = datetime.strptime(last_checkin_time_str, "%Y-%m-%d %H:%M:%S")
            last_checkin_time = last_checkin.time()
            last_checkin_date=last_checkin.date()

            # Get the current time component
            current_time = datetime.now().time()
            current_date = datetime.now().date()
            current_datetime = datetime.now()
            checkin_time=current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            # Compare times
            if last_checkin_time > current_time and current_date==last_checkin_date :
                visitor_manager.insert_visitor(visitor_id,visitor_name,visitor_contact,purpose,host,company,photo_path,government_id_proof_path,checkin_time)
                visitor_manager.update_visitor_status(visitor_id,"Approved")
                result=preapproval_manager.delete_preapproval(visitor_id)
                if(result):
                    st.success("Pre-Approval Storage Freed")
                else:
                    st.warning("Pre-Approval cannot freed")   
            else:
                st.warning(f"{visitor_name} is not eligible for Visit!! Since He/She is late for visit")
        else:
            st.warning(f"{visitor_id} has No Pre-Approval!! Don't let him in")
            
            
            