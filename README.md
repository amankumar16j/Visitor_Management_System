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
Ensure you have **Python 3.10+** installed. You can download it from [python.org](https://www.python.org/downloads/).

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
![image](https://github.com/user-attachments/assets/efb6620b-ffa7-4b6b-ae43-47ff37d4c6cc)
1. Navigate to the **Login** page.
2. Enter the following credentials:
   - **Username:** `Admin`
   - **Password:** `Admin@1234`
3. Click **Login**.
4. Once logged in, go to **Admin Role**.
5. You can **create a user**, **delete a user**, or **view user details**.

### To create user -> fill the information -> select user role -> click sign up 
![image](https://github.com/user-attachments/assets/56b683c4-4ca4-46a2-b74e-2537f8cf6200)
![image](https://github.com/user-attachments/assets/73c5f43c-77c2-4b2e-ab93-fecdaf6a432e)

### To View details of users-> in "Select Your Action" -> select "List User Details"
![image](https://github.com/user-attachments/assets/19cb2558-031e-4150-8d8a-45758c4ece6c)

### To delete a users-> in "Select Your Action" -> select "Delete User" -> fill Username -> click "Delete User" button
![image](https://github.com/user-attachments/assets/91e2b30c-a938-46a3-b82c-6bbc6898e7ca)


## 🏠 Host Login Guide
![image](https://github.com/user-attachments/assets/f6ad0344-eb1b-4184-9a95-d32da5e9e091)
1. Navigate to the **Login** page.
2. Enter the following credentials:
   - **Username:** `Raj Kumar`
   - **Password:** `Raj1234`
3. Click **Login**.
4. Once logged in, go to **Admin Role**.
5. You can **Approve Visitor Request**, **Generate Preapproval**, and **Show Visitors Details**.

### To approve the visitor Request 
![image](https://github.com/user-attachments/assets/26a719a6-576d-404c-a00b-721303b35153)
### To generate Pre-Approval -> fill the information -> click Register Pre-Approval
![image](https://github.com/user-attachments/assets/da15898d-6f32-4f52-b97d-6f9db731bfbd)
![image](https://github.com/user-attachments/assets/47d05b35-1197-44d0-ba6d-9084c86cf698)
### Show my Visitor let you see all the visiter under a particular host
![image](https://github.com/user-attachments/assets/7fec0926-356b-4aae-aef2-0e1466943c02)




## 🔒 Security Login Guide
![image](https://github.com/user-attachments/assets/c94bbfa6-82cc-461a-a521-b93c2ef6f761)
1. Navigate to the **Login** page.
2. Enter the following credentials:
   - **Username:** `Aman Kumar`
   - **Password:** `Aman1234`
3. Click **Login**.
4. Once logged in, go to **Admin Role**.
5. You can **Register Visitor**, **Validate Pre-Approval Check-in**, and **Check Out Visitor**.

### Register Visitor
![image](https://github.com/user-attachments/assets/2ba15fe7-ba8e-4558-9215-38756f568350)
### After filling details and clicking register
![image](https://github.com/user-attachments/assets/1fa22e7e-3e51-4a2a-8789-957cba65bc7b)
### After Approval by host complete verification by checking visitor status
![image](https://github.com/user-attachments/assets/e8ae0a44-0761-422b-9fe6-73675bddb1dc)
### To checkout Visitor enter the visitor_id and click check out
![image](https://github.com/user-attachments/assets/74fca7d7-43c6-4ae3-93a3-f4e5f011ba2c)


## To run the Host, Security, and Admin servers in parallel, follow these steps:

1. **Open Three Terminal Windows**  
   You need to run three instances of Streamlit on different ports.

2. **Run the Admin Server**  
   ```bash
   streamlit run app.py --server.port 8501
   ```

3. **Run the Host Server**  
   ```bash
   streamlit run app.py --server.port 8502
   ```

4. **Run the Security Server**  
   ```bash
   streamlit run app.py --server.port 8503
   ```

Each server will now be accessible on its respective port:
- **Admin Panel** → `http://localhost:8501`
- **Host Panel** → `http://localhost:8502`
- **Security Panel** → `http://localhost:8503`

## Demo Video 
https://drive.google.com/file/d/11P2of7gfuAI4K2KGVpt1D0MdA9XHtrdf/view?usp=sharing

## Documentation
https://drive.google.com/file/d/1iovrOLaDTxjjRwRuX8CasnwgpnGJBAI3/view?usp=sharing

## 🛡️ Security Measures
- **Password Hashing**: Secure authentication with bcrypt.
- **Database Security**: Using SQLite3 with proper data handling.

## 📜 License
This project is licensed under the MIT License.

---

# 📌 Visitor Management System  

The **Visitor Management System** is a web-based application designed to efficiently manage visitors in an organization. It helps track visitor details, their purpose of visit, check-in and check-out times, and host details.  

---

## 🚀 Features  

✅ **User Authentication** – Secure login for administrators, hosts, and security personnel.  
✅ **Visitor Registration** – Capture visitor details like name, contact, and purpose of visit.  
✅ **Host Notification** – Automatically notify hosts when a visitor arrives.  
✅ **Check-in & Check-out System** – Log entry and exit times efficiently.  
✅ **Visitor Badge Generation** – Generate and print visitor badges.  
✅ **Data Analytics & Reports** – Track visitor statistics and generate reports.  
✅ **Search & Filter** – Easily find visitor records.  

---

## 🛠️ Tech Stack  

- **Frontend:** Streamlit  
- **Backend:** Python + Streamlit  
- **Database:** SQLite3  
- **Authentication:** bcrypt  

---

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
├── models/
│   ├── preapproval.py
│   ├── user.py
│   └── visitor.py
├── preapproval_functions/
│   ├── preapproval_registration.py
│   └── validate_preapprovals.py
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
├── requirements.txt
├── users.db
└── visitor_management.db
```

---

## 🚀 Installation and Setup  

### 1️⃣ Install Python  
Ensure **Python 3.10+** is installed. Download it from [python.org](https://www.python.org/downloads/).  

### 2️⃣ Install Dependencies  
Run the following command in the project root directory:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application  
To start the Streamlit app, execute:  
```bash
streamlit run app.py
```

---

## 💂‍♂️ Admin Login Guide  

### Steps to Log in as Admin:  
1. Navigate to the **Login** page.  
2. Enter credentials:  
   - **Username:** `Admin`  
   - **Password:** `Admin@1234`  
3. Click **Login**.  
4. Navigate to **Admin Role** where you can:  
   - **Create Users**  
   - **Delete Users**  
   - **View User Details**  

### 👤 Creating a User:  
1. Fill in the details.  
2. Select a user role.  
3. Click **Sign Up**.  

### 📋 Viewing User Details:  
1. In **"Select Your Action"**, choose **"List User Details"**.  

### ❌ Deleting a User:  
1. In **"Select Your Action"**, choose **"Delete User"**.  
2. Enter the **Username**.  
3. Click **Delete User**.  

---

## 🏠 Host Login Guide  

### Steps to Log in as Host:  
1. Navigate to the **Login** page.  
2. Enter credentials:  
   - **Username:** `Raj Kumar`  
   - **Password:** `Raj1234`  
3. Click **Login**.  
4. Navigate to **Host Role** where you can:  
   - **Approve Visitor Requests**  
   - **Generate Pre-Approvals**  
   - **View Visitor Details**  

### ✅ Approving a Visitor Request:  
1. Open the **Visitor Request** section.  
2. Select a request.  
3. Click **Approve**.  

### 📝 Generating a Pre-Approval:  
1. Fill in visitor details.  
2. Click **Register Pre-Approval**.  

### 📌 Viewing Visitors Assigned to a Host:  
1. Navigate to **Show My Visitors**.  

---

## 🔒 Security Login Guide  

### Steps to Log in as Security:  
1. Navigate to the **Login** page.  
2. Enter credentials:  
   - **Username:** `Aman Kumar`  
   - **Password:** `Aman1234`  
3. Click **Login**.  
4. Navigate to **Security Role** where you can:  
   - **Register Visitors**  
   - **Validate Pre-Approvals**  
   - **Check Out Visitors**  

### 🆕 Registering a Visitor:  
1. Enter visitor details.  
2. Click **Register**.  

### ✅ Validating a Pre-Approval:  
1. Search for the visitor.  
2. Check the visitor's status.  

### ⏳ Checking Out a Visitor:  
1. Enter the **Visitor ID**.  
2. Click **Check Out**.  

---

## 🌐 Running Multiple Servers (Admin, Host, Security)  

To run the **Admin, Host, and Security** servers simultaneously, follow these steps:

1️⃣ **Open three terminal windows**.  
2️⃣ **Run the Admin server**:  
```bash
streamlit run app.py --server.port 8501
```  
3️⃣ **Run the Host server**:  
```bash
streamlit run app.py --server.port 8502
```  
4️⃣ **Run the Security server**:  
```bash
streamlit run app.py --server.port 8503
```  

### 🔗 Access the panels here:  
- **Admin Panel** → `http://localhost:8501`  
- **Host Panel** → `http://localhost:8502`  
- **Security Panel** → `http://localhost:8503`  

---

## 🎥 Demo Video  
🔗 [Watch the Demo](https://drive.google.com/file/d/11P2of7gfuAI4K2KGVpt1D0MdA9XHtrdf/view?usp=sharing)  

## 📜 Documentation  
📄 [Read Full Documentation](https://drive.google.com/file/d/1iovrOLaDTxjjRwRuX8CasnwgpnGJBAI3/view?usp=sharing)  

---

## 🛡️ Security Measures  

🔹 **Password Hashing** – Secure authentication with bcrypt.  
🔹 **Database Security** – SQLite3 with secure data handling.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

### ✅ What’s Improved?  
✔️ **Better Formatting & Spacing**  
✔️ **Clear Step-by-Step Instructions**  
✔️ **Readable and Well-Organized Sections**  

Now your README looks professional and is easy to follow! 🚀 Let me know if you need any further refinements. 😊
