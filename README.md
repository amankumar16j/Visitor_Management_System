Here’s the improved README with properly formatted text **and** image placeholders. Just replace the image links with the correct ones from your repository or hosting service.

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

![Admin Login](https://github.com/user-attachments/assets/efb6620b-ffa7-4b6b-ae43-47ff37d4c6cc)  

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
![Create User](https://github.com/user-attachments/assets/56b683c4-4ca4-46a2-b74e-2537f8cf6200)  

### 📋 Viewing User Details:  
![View Users](https://github.com/user-attachments/assets/19cb2558-031e-4150-8d8a-45758c4ece6c)  

### ❌ Deleting a User:  
![Delete User](https://github.com/user-attachments/assets/91e2b30c-a938-46a3-b82c-6bbc6898e7ca)  

---

## 🏠 Host Login Guide  

![Host Login](https://github.com/user-attachments/assets/f6ad0344-eb1b-4184-9a95-d32da5e9e091)  

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
![Approve Visitor](https://github.com/user-attachments/assets/26a719a6-576d-404c-a00b-721303b35153)  

### 📝 Generating a Pre-Approval:  
![Pre-Approval](https://github.com/user-attachments/assets/da15898d-6f32-4f52-b97d-6f9db731bfbd)  

### 📌 Viewing Visitors Assigned to a Host:  
![Show My Visitors](https://github.com/user-attachments/assets/7fec0926-356b-4aae-aef2-0e1466943c02)  

---

## 🔒 Security Login Guide  

![Security Login](https://github.com/user-attachments/assets/c94bbfa6-82cc-461a-a521-b93c2ef6f761)  

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
![Register Visitor](https://github.com/user-attachments/assets/2ba15fe7-ba8e-4558-9215-38756f568350)  

### ✅ Validating a Pre-Approval:  
![Validate Visitor](https://github.com/user-attachments/assets/e8ae0a44-0761-422b-9fe6-73675bddb1dc)  

### ⏳ Checking Out a Visitor:  
![Check Out](https://github.com/user-attachments/assets/74fca7d7-43c6-4ae3-93a3-f4e5f011ba2c)  

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

### ✅ What’s Improved?  
✔️ **Proper Spacing & Readability**  
✔️ **Clear Step-by-Step Instructions**  
✔️ **Formatted Sections with Relevant Images**  

Your README now looks professional and user-friendly! 🚀 Let me know if you need any final refinements. 😊
