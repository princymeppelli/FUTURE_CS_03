## 🔐 Secure File Sharing System

# Project Overview
This project is a secure web-based file sharing system developed to demonstrate how sensitive files can be protected during storage and access. The main focus of this project is security. Files uploaded to the system are encrypted before being stored, and only authorized users are allowed to download and decrypt them.
The project simulates real-world use cases such as secure document sharing in organizations, educational institutions, or internal company systems where data confidentiality is important.

# Objectives
•	To allow users to upload files securely
•	To encrypt files before storing them on the server
•	To restrict file downloads using authentication
•	To ensure encrypted files are unreadable without proper authorization
•	To provide a simple and user-friendly interface

# Key Features
•	Public file upload functionality
•	AES (Advanced Encryption Standard) encryption for all uploaded files
•	Encrypted file storage (files are unreadable at rest)
•	Login-based authentication for file downloads
•	Session-based access control
•	Re-authentication required for every download
•	Clean and modern user interface with pop-up 

# Technologies Used
•	Python – Backend logic
•	Flask – Web framework
•	AES Encryption (PyCryptodome) – File encryption and decryption
•	HTML, CSS, JavaScript – Frontend design
•	Flask Sessions – Authentication handling

# Security Implementation
•	Files are encrypted using AES-256 encryption before being stored on the server
•	A persistent secret key is used to ensure correct decryption across sessions
•	Encrypted files cannot be opened directly from the server storage
•	File download is allowed only after successful login
•	Session is cleared after every download to enforce strict access control

# Application Flow
1.	User uploads a file
2.	File is encrypted and stored securely
3.	Encrypted files can be viewed in the system
4.	When download is requested, login is required
5.	After successful authentication, file is decrypted and downloaded
6.	User session is cleared after download

# How to Run the Project
1.	Clone or download the repository
2.	Create and activate a virtual environment
3.	Install required dependencies
4.	Run the Flask application
5.	Open the application in a browser
python app.py
Open browser and go to:
http://127.0.0.1:5000

Login Credentials
Username: admin  
Password: admin123

# Project Structure
secure_file_sharing/
│
├── app.py
├── secret.key
├── uploads/
├── templates/
│   ├── index.html
│   ├── files.html
│   └── login.html
└── static/
    ├── bg.png
    └── login_bg.png
    
## Future Enhancements
•	User registration system
•	Role-based access control
•	Database integration
•	Improved key management using environment variables
•	Audit logs for file downloads

 # Conclusion:
This project demonstrates a practical implementation of secure file handling using encryption and authentication techniques. It highlights the importance of protecting data at rest and controlling access to sensitive resources, making it suitable for academic, internship, and learning purposes.
Meppelli Princy
Cyber Security Intern | BCA Student
