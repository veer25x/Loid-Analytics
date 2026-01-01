# Loid-Analytics(https://loid-analytics.onrender.com)
Professional AI education platform with certificate management. Generate verifiable certificates, browse courses/internships, full admin dashboard. Modern UI, Python/Flask backend, Tailwind CSS frontend. Perfect for educational institutions &amp; certification programs.
🎯 Key Highlights
Professional Certificate Generation with unique IDs

Instant Certificate Verification system

Modern, Responsive UI with dark/light themes

Comprehensive Admin Dashboard for management

Secure Authentication and data protection

✨ Features
🎓 For Students/Learners
Browse Courses: Explore AI, ML, and Data Science courses

Find Internships: Discover real-world internship opportunities

Generate Certificates: Create professional certificates for completed courses

Verify Certificates: Authenticate certificate legitimacy

Responsive Design: Accessible on all devices

🛠️ For Administrators
Dashboard Analytics: Real-time statistics and charts

Certificate Management: Add, edit, revoke, and delete certificates

Course Management: Manage course catalog and content

User Management: Handle user accounts and permissions

System Settings: Configure platform settings and security

🚀 Technical Features
Modern UI/UX: Beautiful gradient designs with animations

Dark/Light Mode: Theme toggle for user preference

PDF Generation: Professional certificate PDF downloads

Data Visualization: Interactive charts and graphs

RESTful API: Clean API endpoints for integration
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Git

Step-by-Step Setup
Clone the Repository

bash
git clone https://github.com/yourusername/loid-analytics-platform.git
cd loid-analytics-platform
Create Virtual Environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
Configure Environment Variables

bash
# Create .env file
cp .env.example .env
# Edit .env with your configurations
Initialize Database

bash
# The system will auto-create necessary data files
python app.py
Run the Application

bash
python app.py
Access the Application

Main Application: http://localhost:5000

Admin Panel: http://localhost:5000/admin/login

Default Admin Credentials:

Username: admin

Password: admin123

📁 Project Structure
text
loid-analytics-platform/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .env.example               # Environment variables template
│
├── data/                      # Data storage
│   ├── certificates.json      # Certificate database
│   └── users.json            # User database (if implemented)
│
├── static/                    # Static assets
│   ├── css/                  # Custom CSS files
│   ├── js/                   # JavaScript files
│   ├── images/               # Images and icons
│   └── certificates/         # Generated certificate PDFs
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   ├── index.html            # Homepage
│   ├── courses.html          # Courses page
│   ├── internships.html      # Internships page
│   ├── certificate.html      # Certificate generator
│   ├── verify.html           # Certificate verification
│   ├── admin.html            # Admin dashboard
│   └── admin_login.html      # Admin login page
│
└── README.md                  # Project documentation
