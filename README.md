# Patient_apis
Janitri Backend Assignment - Patient Monitoring System

Overview

This project is a backend API for managing patients and their heart rate data. It is built using Django and Django REST Framework (DRF). The system allows user registration, patient management, and heart rate monitoring.

Features

User Registration & Login (Simple email-password authentication)

Manage Patients (Add, update, retrieve patient details)

Heart Rate Data (Record and retrieve heart rate data for patients)

RESTful API Design

Secure Data Handling

Error Handling & Validation

Modular & Extendable Codebase

Token-based Authentication (Optional)

Unit Testing (Optional)

Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (Can be replaced with PostgreSQL/MySQL)

Authentication: Basic email-password validation

Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/yourusername/Patient_apis.git
cd Patient_apis

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create a Superuser

python manage.py createsuperuser

6️⃣ Run the Server

python manage.py runserver

API Endpoints

🔹 User Authentication

Endpoint

Method

Description

/api/register/
POST
Register a new user

/api/login/
POST
Login user

Request Example - Registration (/api/register/)

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpassword"
}

Response Example

{
  "message": "User registered successfully!"
}

🔹 Patients Management

Endpoint

Method

Description

/api/patients/
POST
Add a new patient

/api/patients/
GET
Get all patients

/api/patients/{id}/
GET
Get a specific patient by ID

Request Example - Add Patient (/api/patients/)

{
  "name": "John Doe",
  "age": 30,
  "gender": "Male"
}

🔹 Heart Rate Data

Endpoint

Method

Description

/api/heart-rate/

POST

Record heart rate for a patient
/api/heart-rate/{patient_id}/

GET
retrieve heart rate data for a patient

Assumptions & Decisions

Basic authentication is used for simplicity (email & password validation without OAuth/JWT).

No real-time monitoring is implemented, but the system can be extended for live data processing.

Data relationships: A Patient has multiple heart rate records.

Folder Structure

Patient_apis/
│── patient_ms/  # Main Django project folder
│   ├── settings.py  # Django settings
│   ├── urls.py  # Project-level URLs
│   ├── wsgi.py  # WSGI entry point
│── patientapp/  # Main app for managing patients
│   ├── models.py  # Database models
│   ├── views.py  # API views
│   ├── serializers.py  # DRF Serializers
│   ├── urls.py  # App-level URLs
│   ├── tests.py  # Unit tests
│── users/  # User authentication app
│   ├── models.py  # Custom user model
│   ├── views.py  # Authentication views
│   ├── serializers.py  # Serializers for authentication
│── requirements.txt  # Python dependencies
│── manage.py  # Django management script
│── README.md  # Project documentation

How to Contribute 🤝

Fork the repository.
Create a new branch (feature-branch).
Commit your changes.
Push to your branch and create a PR.

License
This project is open-source and available under the MIT License.

Contact
For any questions, reach out via ishan19112000@gmail.com. 🚀

