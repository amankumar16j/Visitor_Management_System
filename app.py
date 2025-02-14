import streamlit as st
from views.login import login
from views.signup import signup
from views.delete import delete
from views.admin_dashboard import admin_dashboard
from views.dashboard import dashboard
import streamlit as st
from functions.visitor_registration import visitor_registration
from functions.approval_portal import approval_portal
from functions.checkapproval import visitor_status
from functions.checkout import check_out_visitor

# from views.register_user import register

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = None

st.sidebar.title("Navigation")
choice = st.sidebar.selectbox("Go to", ["Login","Security Role","Admin Role","Host","Dashboard"])


if choice == "Login":
    login()
    
elif choice == "Admin Role":
    if st.session_state.authenticated:
        if st.session_state.role == "Admin":
            st.title("Action You Want To Perform")
            Action = st.selectbox("Select Your Action", ["Register User", "Delete User","List User Detail"],index=0)
            if(Action=="Register User"):
                signup()
            if(Action=="Delete User"):
                delete()
            if(Action=="List User Detail"):
                admin_dashboard()     
        else:
           st.warning("You are not allowed to access admin dashboard")
    else:
        st.warning("Please log in to access admin dashboard.")
   
        
elif choice=="Security Role":
    if st.session_state.authenticated:
        if st.session_state.role == "Security":
            st.title("Action You Want To Perform")
            Action2 = st.selectbox("Select Your Action", ["Select Action","Register Visitor", "Check Out Visitor"],index=0)
            if Action2=="Register Visitor":
                visitor_registration()
                visitor_status()
            if Action2== "Check Out Visitor":
                check_out_visitor()
            if Action2=="Select Action":
                st.warning("Select any Action from Selector to Proceed")
        else:
           st.warning("You are not allowed to access Security dashboard")
    else:
        st.warning("Please log in to access Security dashboard.")

elif choice=="Host":
    if st.session_state.authenticated:
        if st.session_state.role == "Host":
            approval_portal()
        else:
           st.warning("You are not allowed to access this funtion")
    else:
        st.warning("Please log in to access the dashboard.")
 
elif choice == "Dashboard":
    if st.session_state.authenticated:
        if st.session_state.role == "admin":
            admin_dashboard()
        else:
            dashboard()
    else:
        st.warning("Please log in to access the dashboard.")

if st.sidebar.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.role = None
    st.session_state.username = None
    st.experimental_rerun()
