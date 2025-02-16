# Visitor Management System

## 📌 Project Overview
The **Visitor Management System** is a web-based application designed to streamline the process of managing visitors in an organization. It helps maintain records of visitor details, their purpose of visit, check-in and check-out times, and host details.

## 🚀 Features
- **User Authentication**: Secure login for administrators and receptionists.
- **Visitor Registration**: Capture visitor details such as name, contact, and purpose of visit.
- **Host Notification**: Automatically notify the host about the visitor’s arrival.
- **Check-in & Check-out System**: Record entry and exit times.
- **Visitor Badge Generation**: Generate printable visitor badges.
- **Data Analytics & Reports**: Track visitor statistics and generate reports.
- **Search & Filter**: Easily search for visitor records.

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python + Streamlit  
- **Database:** SQLite3  
- **Authentication:** bcrypt  

## 📂 Project Structure
```
Visitor-Management-System/
├── db/
│   ├── memberdatabase.py
│   ├── pre_approval_database.py
│   └── visitordatabase.py
├── functions/
│   ├── approval_portal.py
│   ├── checkapproval.py
│   ├── checkout.py
│   ├── generate_identity_card.py
│   ├── generate_visitor_id.py
│   ├── qr_generator.py
│   └── visitor_registration.py
├── government_id_proof/
├── models/
│   ├── preapproval.py
│   ├── user.py
│   └── visitor.py
├── photo/
├── preapproval_functions/
│   ├── preapproval_registration.py
│   └── validate_preapprovals.py
├── qr_code/
├── utils/
│   └── security.py
├── views/
│   ├── admin_dashboard.py
│   ├── dashboard.py
│   ├── delete.py
│   ├── login.py
│   └── signup.py
├── app.py
├── createAdmin.py
├── pre_approval.db
├── requirements.txt
├── users.db
└── visitor_management.db
```

## 🚀 Installation and Setup

### 1️⃣ Install Python
Ensure you have **Python 3.8+** installed. You can download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Install Dependencies
Run the following command in the project root directory to install required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application
To start the Streamlit application, use:
```bash
streamlit run app.py
```

## 💂️ Admin Login Guide

1. Navigate to the **Login** page.
2. Enter the following credentials:
   - **Username:** `Admin`
   - **Password:** `Admin@1234`
3. Click **Login**.
4. Once logged in, go to **Admin Role**.
5. You can **create a user**, **delete a user**, or **view user details**.

## 🏠 Host Login Guide

1. Navigate to the **Login** page.
2. Enter the following credentials:
   - **Username:** `Raj Kumar`
   - **Password:** `Raj1234`
3. Click **Login**.
4. Once logged in, go to **Admin Role**.
5. You can **Approve Visitor Request**, **Generate Preapproval**, and **Show Visitors Details**.

## 🔒 Security Login Guide

1. Navigate to the **Login** page.
2. Enter the following credentials:
   - **Username:** `Aman Kumar`
   - **Password:** `Aman1234`
3. Click **Login**.
4. Once logged in, go to **Admin Role**.
5. You can **Register Visitor**, **Validate Pre-Approval Check-in**, and **Check Out Visitor**.

## 🛡️ Security Measures
- **Password Hashing**: Secure authentication with bcrypt.
- **Database Security**: Using SQLite3 with proper data handling.

## 📜 License
This project is licensed under the MIT License.

---
