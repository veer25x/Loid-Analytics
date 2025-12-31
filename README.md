# Loid-Analytics
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

code:-

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veer Pratap Singh | AI & ML Engineer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Raleway:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        /* Custom Color Scheme for Veer - Tech + Innovation */
        :root {
            --primary-color: #4f46e5; /* Indigo */
            --secondary-color: #7c3aed; /* Purple */
            --dark-color: #0f172a; /* Dark blue */
            --light-color: #f8fafc; /* Light background */
            --accent-color: #06b6d4; /* Cyan accent */
            --gray-color: #64748b;
            --transition: all 0.3s ease;
            --shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            --radius: 10px;
            --gradient: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.7;
            color: var(--dark-color);
            background-color: var(--light-color);
        }

        h1, h2, h3, h4 {
            font-family: 'Raleway', sans-serif;
            font-weight: 700;
            line-height: 1.2;
            margin-bottom: 1rem;
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }

        section {
            padding: 100px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 60px;
            position: relative;
            font-size: 2.5rem;
        }

        .section-title:after {
            content: '';
            position: absolute;
            width: 80px;
            height: 5px;
            background: var(--gradient);
            bottom: -15px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 3px;
        }

        .btn {
            display: inline-block;
            padding: 14px 32px;
            background: var(--gradient);
            color: white;
            border-radius: var(--radius);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
            border: none;
            cursor: pointer;
            font-size: 1rem;
            letter-spacing: 0.5px;
        }

        .btn:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid var(--primary-color);
            color: var(--primary-color);
        }

        .btn-outline:hover {
            background: var(--gradient);
            color: white;
            border-color: transparent;
        }

        /* Header & Navigation */
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background-color: rgba(255, 255, 255, 0.98);
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.08);
            padding: 20px 0;
            transition: var(--transition);
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 2rem;
            font-weight: 800;
            color: var(--primary-color);
            text-decoration: none;
        }

        .logo span {
            color: var(--accent-color);
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 35px;
        }

        nav ul li a {
            text-decoration: none;
            color: var(--dark-color);
            font-weight: 600;
            transition: var(--transition);
            position: relative;
            font-size: 1.1rem;
        }

        nav ul li a:hover {
            color: var(--primary-color);
        }

        nav ul li a.active {
            color: var(--primary-color);
        }

        nav ul li a.active:after {
            width: 100%;
        }

        nav ul li a:after {
            content: '';
            position: absolute;
            width: 0;
            height: 3px;
            background: var(--gradient);
            bottom: -5px;
            left: 0;
            transition: var(--transition);
        }

        nav ul li a:hover:after {
            width: 100%;
        }

        .mobile-toggle {
            display: none;
            font-size: 1.8rem;
            cursor: pointer;
            color: var(--dark-color);
        }

        /* Hero Section - Without Photo */
        .hero {
            padding-top: 180px;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4edf5 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
        }

        .hero:before {
            content: '';
            position: absolute;
            width: 500px;
            height: 500px;
            border-radius: 50%;
            background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(124, 58, 237, 0.1) 100%);
            top: -100px;
            right: -100px;
        }

        .hero-content {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            position: relative;
            z-index: 1;
            text-align: center;
        }

        .hero-text {
            flex: 1;
            min-width: 300px;
            max-width: 800px;
        }

        .hero-text h1 {
            font-size: 3.5rem;
            margin-bottom: 15px;
            line-height: 1.1;
        }

        .hero-text .subtitle {
            font-size: 1.8rem;
            color: var(--gray-color);
            margin-bottom: 20px;
            font-weight: 500;
        }

        .hero-text .highlight {
            background: var(--gradient);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            padding: 0 5px;
        }

        .hero-text p {
            font-size: 1.2rem;
            color: var(--gray-color);
            margin-bottom: 35px;
            max-width: 700px;
            margin-left: auto;
            margin-right: auto;
        }

        .hero-btns {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 40px;
        }

        /* AI/ML Badge */
        .ai-badge {
            display: inline-flex;
            align-items: center;
            background: rgba(6, 182, 212, 0.1);
            color: var(--accent-color);
            padding: 10px 20px;
            border-radius: 30px;
            font-weight: 600;
            margin-bottom: 30px;
            border: 2px solid rgba(6, 182, 212, 0.2);
        }

        .ai-badge i {
            margin-right: 10px;
            font-size: 1.2rem;
        }

        .social-links {
            display: flex;
            justify-content: center;
            margin-top: 40px;
            flex-wrap: wrap;
            gap: 15px;
        }

        .social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            background-color: white;
            border-radius: 50%;
            color: var(--dark-color);
            text-decoration: none;
            transition: var(--transition);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            font-size: 1.2rem;
        }

        .social-links a:hover {
            background: var(--gradient);
            color: white;
            transform: translateY(-8px);
        }

        /* About Section */
        .about-content {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 50px;
        }

        .about-text {
            flex: 1;
            min-width: 300px;
        }

        .about-text h2 {
            font-size: 2.8rem;
            margin-bottom: 25px;
        }

        .about-text p {
            margin-bottom: 20px;
            color: var(--gray-color);
            font-size: 1.1rem;
        }

        .education-card {
            background: white;
            border-radius: var(--radius);
            padding: 30px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            margin-top: 30px;
            border-left: 5px solid var(--primary-color);
        }

        .education-card h3 {
            color: var(--primary-color);
            margin-bottom: 10px;
        }

        .education-card .year {
            color: var(--accent-color);
            font-weight: 600;
            margin-bottom: 15px;
            display: block;
        }

        /* Skills Section */
        .skills-section {
            background-color: #f8f9fa;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 30px;
        }

        .skill-card {
            background: white;
            border-radius: var(--radius);
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            transition: var(--transition);
        }

        .skill-card:hover {
            transform: translateY(-10px);
            box-shadow: var(--shadow);
        }

        .skill-icon {
            font-size: 3rem;
            margin-bottom: 20px;
            color: var(--primary-color);
        }

        .skill-card h3 {
            font-size: 1.4rem;
            margin-bottom: 10px;
        }

        /* Projects Section */
        .projects {
            background-color: white;
        }

        .projects-filter {
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
            flex-wrap: wrap;
            gap: 10px;
        }

        .filter-btn {
            padding: 10px 25px;
            background-color: #f1f5f9;
            border: none;
            border-radius: 30px;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition);
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
        }

        .filter-btn.active, .filter-btn:hover {
            background: var(--gradient);
            color: white;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 35px;
        }

        .project-card {
            background-color: white;
            border-radius: var(--radius);
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            transition: var(--transition);
            border: 1px solid #f1f5f9;
        }

        .project-card:hover {
            transform: translateY(-15px);
            box-shadow: var(--shadow);
        }

        .project-img {
            height: 200px;
            overflow: hidden;
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary-color);
            font-size: 4rem;
        }

        .project-info {
            padding: 30px;
        }

        .project-info h3 {
            font-size: 1.5rem;
            margin-bottom: 15px;
        }

        .project-info p {
            color: var(--gray-color);
            margin-bottom: 20px;
        }

        .project-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 20px;
        }

        .project-tags span {
            background-color: #e9f2ff;
            color: var(--primary-color);
            padding: 6px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .project-links {
            display: flex;
            gap: 10px;
        }

        /* Experience & Education */
        .timeline {
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }

        .timeline:before {
            content: '';
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 3px;
            height: 100%;
            background-color: #e9ecef;
        }

        .timeline-item {
            margin-bottom: 50px;
            position: relative;
            width: 50%;
            padding-right: 60px;
        }

        .timeline-item:nth-child(even) {
            margin-left: 50%;
            padding-right: 0;
            padding-left: 60px;
        }

        .timeline-item:last-child {
            margin-bottom: 0;
        }

        .timeline-dot {
            position: absolute;
            top: 0;
            right: -12px;
            width: 24px;
            height: 24px;
            background: var(--gradient);
            border-radius: 50%;
            z-index: 1;
            box-shadow: 0 0 0 5px white;
        }

        .timeline-item:nth-child(even) .timeline-dot {
            right: auto;
            left: -12px;
        }

        .timeline-content {
            background-color: white;
            padding: 30px;
            border-radius: var(--radius);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            position: relative;
        }

        .timeline-content:before {
            content: '';
            position: absolute;
            top: 20px;
            right: -10px;
            width: 0;
            height: 0;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
            border-left: 10px solid white;
        }

        .timeline-item:nth-child(even) .timeline-content:before {
            right: auto;
            left: -10px;
            border-left: none;
            border-right: 10px solid white;
        }

        .timeline-content h3 {
            font-size: 1.4rem;
            margin-bottom: 8px;
        }

        .timeline-content .date {
            color: var(--primary-color);
            font-weight: 600;
            margin-bottom: 12px;
            display: block;
            font-size: 1rem;
        }

        .timeline-content p {
            color: var(--gray-color);
        }

        /* Contact Section */
        .contact {
            background: linear-gradient(135deg, var(--dark-color) 0%, #1e293b 100%);
            color: white;
        }

        .contact .section-title {
            color: white;
        }

        .contact .section-title:after {
            background-color: var(--accent-color);
        }

        .contact-content {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 50px;
        }

        .contact-info {
            flex: 1;
            min-width: 300px;
        }

        .contact-info p {
            margin-bottom: 30px;
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .contact-details {
            margin-top: 40px;
        }

        .contact-item {
            display: flex;
            align-items: center;
            margin-bottom: 25px;
        }

        .contact-item i {
            background-color: rgba(255, 255, 255, 0.1);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 20px;
            font-size: 1.5rem;
            color: var(--accent-color);
        }

        .contact-form {
            flex: 1;
            min-width: 300px;
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 18px;
            border: none;
            border-radius: var(--radius);
            background-color: rgba(255, 255, 255, 0.1);
            color: white;
            font-family: 'Poppins', sans-serif;
            font-size: 1rem;
            transition: var(--transition);
        }

        .form-group textarea {
            min-height: 180px;
            resize: vertical;
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            background-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1);
        }

        .form-group input::placeholder,
        .form-group textarea::placeholder {
            color: rgba(255, 255, 255, 0.6);
        }

        /* Footer */
        footer {
            background-color: #0d1117;
            color: #8b949e;
            padding: 60px 0 30px;
        }

        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 40px;
        }

        .footer-logo {
            font-size: 2rem;
            font-weight: 800;
            color: white;
            text-decoration: none;
        }

        .footer-logo span {
            color: var(--accent-color);
        }

        .copyright {
            text-align: center;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            width: 100%;
            font-size: 0.95rem;
        }

        /* Responsive Design */
        @media (max-width: 1100px) {
            .hero-text h1 {
                font-size: 3rem;
            }
        }

        @media (max-width: 992px) {
            .hero-text h1 {
                font-size: 2.8rem;
            }
            
            .section-title {
                font-size: 2.2rem;
            }
        }

        @media (max-width: 768px) {
            .mobile-toggle {
                display: block;
            }

            nav {
                position: fixed;
                top: 90px;
                right: -100%;
                width: 85%;
                height: calc(100vh - 90px);
                background-color: white;
                box-shadow: -10px 0 30px rgba(0, 0, 0, 0.1);
                transition: var(--transition);
                padding: 40px;
            }

            nav.active {
                right: 0;
            }

            nav ul {
                flex-direction: column;
            }

            nav ul li {
                margin: 0 0 25px 0;
            }

            nav ul li a {
                font-size: 1.3rem;
            }

            .hero, section {
                padding: 80px 0;
            }

            .hero {
                padding-top: 140px;
                min-height: auto;
            }

            .about-content, .contact-content {
                flex-direction: column;
            }

            .about-text, .contact-info, .contact-form {
                margin-bottom: 50px;
            }

            .hero-text h1 {
                font-size: 2.5rem;
            }

            .hero-text .subtitle {
                font-size: 1.5rem;
            }

            .timeline:before {
                left: 30px;
            }

            .timeline-item {
                width: 100%;
                padding-right: 0;
                padding-left: 70px;
            }

            .timeline-item:nth-child(even) {
                margin-left: 0;
                padding-left: 70px;
            }

            .timeline-dot {
                left: 18px;
                right: auto;
            }

            .timeline-item:nth-child(even) .timeline-dot {
                left: 18px;
            }

            .timeline-content:before {
                display: none;
            }
        }

        @media (max-width: 576px) {
            .hero-text h1 {
                font-size: 2.2rem;
            }
            
            .section-title {
                font-size: 1.8rem;
            }
            
            .hero-btns {
                flex-direction: column;
                width: 100%;
            }
            
            .btn {
                width: 100%;
                text-align: center;
                margin-bottom: 10px;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
            
            .skills-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Header & Navigation -->
    <header>
        <div class="container header-content">
            <a href="#" class="logo">Veer<span>.</span></a>
            <div class="mobile-toggle">
                <i class="fas fa-bars"></i>
            </div>
            <nav>
                <ul>
                    <li><a href="#home" class="active">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#skills">Skills</a></li>
                    <li><a href="#projects">Projects</a></li>
                    <li><a href="#experience">Experience</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="container hero-content">
            <div class="hero-text">
                <div class="ai-badge">
                    <i class="fas fa-robot"></i> AI & ML Engineering Student
                </div>
                <h1>Hi, I'm <span class="highlight">Veer Pratap Singh</span></h1>
                <div class="subtitle">Building Intelligent Systems for Tomorrow</div>
                <p>I'm an enthusiastic AI and ML Engineering student passionate about cutting-edge technology. I specialize in developing intelligent systems and have a keen interest in deep learning, neural networks, and real-world AI applications.</p>
                
                <div class="hero-btns">
                    <a href="#projects" class="btn">View My Projects</a>
                    <a href="#contact" class="btn btn-outline">Contact Me</a>
                </div>
                
                <div class="social-links">
                    <a href="https://github.com/veer25x" target="_blank"><i class="fab fa-github"></i></a>
                    <a href="https://www.linkedin.com/in/veer-pratap-singh-9447a21aa" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                    <a href="https://twitter.com/Veer_is_Veer" target="_blank"><i class="fab fa-twitter"></i></a>
                    <a href="https://instagram.com/veer_is_veer" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="mailto:veerofficial429@gmail.com"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <h2>My Journey in AI & ML</h2>
                    <p>I'm Veer Pratap Singh from Jaunpur, Uttar Pradesh, currently pursuing my B.Tech in Computer Science with specialization in Artificial Intelligence and Machine Learning at Sanskriti University (2023-2027).</p>
                    <p>My journey into technology began with a fascination for how machines can learn and make decisions. This curiosity evolved into a passion for building intelligent systems that can solve complex real-world problems.</p>
                    <p>When I'm not coding or studying ML algorithms, I enjoy exploring new technologies, contributing to open-source projects, and mentoring fellow students in AI/ML concepts.</p>
                    
                    <div class="education-card">
                        <h3>Sanskriti University</h3>
                        <span class="year">2023 - 2027</span>
                        <p>B.Tech in Computer Science & Engineering<br>
                        Specialization: Artificial Intelligence & Machine Learning<br>
                        Positions: Class Representative & Innovation Club President</p>
                    </div>
                </div>
                
                <div class="about-text">
                    <h2>Leadership & Achievements</h2>
                    <p>Throughout my academic journey, I've taken on leadership roles that have shaped my skills:</p>
                    
                    <div style="margin-top: 30px;">
                        <h3><i class="fas fa-award" style="color: var(--accent-color); margin-right: 10px;"></i> School Leadership</h3>
                        <p>Started as Class Monitor and progressed to Blue House Captain, developing early leadership and organizational skills.</p>
                        
                        <h3 style="margin-top: 25px;"><i class="fas fa-users" style="color: var(--primary-color); margin-right: 10px;"></i> College Leadership</h3>
                        <p>Served as Class Representative and currently leading as Innovation Club President, organizing AI/ML workshops and hackathons.</p>
                        
                        <h3 style="margin-top: 25px;"><i class="fas fa-certificate" style="color: var(--secondary-color); margin-right: 10px;"></i> Certifications</h3>
                        <p>Completed multiple AI/ML certifications showcased on my LinkedIn profile, continuously updating my skills in this rapidly evolving field.</p>
                    </div>
                    
                    <a href="https://www.linkedin.com/in/veer-pratap-singh-9447a21aa" class="btn" target="_blank" style="margin-top: 30px;">
                        <i class="fab fa-linkedin"></i> View My LinkedIn
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="skills-section">
        <div class="container">
            <h2 class="section-title">My Skills</h2>
            <div class="skills-grid">
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fab fa-python"></i>
                    </div>
                    <h3>Python</h3>
                    <p>Advanced programming for AI/ML applications and data analysis</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3>Machine Learning</h3>
                    <p>Supervised & unsupervised learning algorithms and model development</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fas fa-network-wired"></i>
                    </div>
                    <h3>Deep Learning</h3>
                    <p>Neural networks, CNNs, RNNs, and advanced AI architectures</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h3>TensorFlow/Keras</h3>
                    <p>Building and training deep learning models</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fas fa-database"></i>
                    </div>
                    <h3>Data Science</h3>
                    <p>Data analysis, visualization, and statistical modeling</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fas fa-eye"></i>
                    </div>
                    <h3>Computer Vision</h3>
                    <p>Image processing, object detection, and recognition systems</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fas fa-language"></i>
                    </div>
                    <h3>NLP</h3>
                    <p>Natural Language Processing and text analysis</p>
                </div>
                
                <div class="skill-card">
                    <div class="skill-icon">
                        <i class="fab fa-git-alt"></i>
                    </div>
                    <h3>Git & GitHub</h3>
                    <p>Version control and collaborative development</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <div class="container">
            <h2 class="section-title">My Projects</h2>
            <div class="projects-filter">
                <button class="filter-btn active" data-filter="all">All Projects</button>
                <button class="filter-btn" data-filter="web">Web Development</button>
                <button class="filter-btn" data-filter="ml">Machine Learning</button>
            </div>
            <div class="projects-grid">
                <!-- Web Development Projects -->
                <div class="project-card" data-category="web">
                    <div class="project-img">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <div class="project-info">
                        <h3>Data Analytics Dashboard</h3>
                        <p>Interactive dashboard for data visualization and analysis with real-time charts and reporting features.</p>
                        <div class="project-tags">
                            <span>HTML/CSS</span>
                            <span>JavaScript</span>
                            <span>Chart.js</span>
                            <span>Python</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="btn">View Details</a>
                            <a href="https://github.com/veer25x" class="btn btn-outline" target="_blank">GitHub</a>
                        </div>
                    </div>
                </div>
                
                <div class="project-card" data-category="web">
                    <div class="project-img">
                        <i class="fas fa-shopping-cart"></i>
                    </div>
                    <div class="project-info">
                        <h3>Food Store E-commerce</h3>
                        <p>Full-featured online food ordering system with shopping cart, payment integration, and admin dashboard.</p>
                        <div class="project-tags">
                            <span>React</span>
                            <span>Node.js</span>
                            <span>MongoDB</span>
                            <span>Stripe API</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="btn">View Details</a>
                            <a href="https://github.com/veer25x" class="btn btn-outline" target="_blank">GitHub</a>
                        </div>
                    </div>
                </div>
                
                <div class="project-card" data-category="web">
                    <div class="project-img">
                        <i class="fas fa-tasks"></i>
                    </div>
                    <div class="project-info">
                        <h3>Smart Task Manager</h3>
                        <p>Advanced todo application with task categorization, priority levels, progress tracking, and reminders.</p>
                        <div class="project-tags">
                            <span>JavaScript</span>
                            <span>Local Storage</span>
                            <span>CSS3</span>
                            <span>Responsive</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="btn">View Details</a>
                            <a href="https://github.com/veer25x" class="btn btn-outline" target="_blank">GitHub</a>
                        </div>
                    </div>
                </div>
                
                <!-- ML Projects -->
                <div class="project-card" data-category="ml">
                    <div class="project-img">
                        <i class="fas fa-home"></i>
                    </div>
                    <div class="project-info">
                        <h3>House Price Prediction</h3>
                        <p>ML model predicting real estate prices using regression algorithms and feature engineering.</p>
                        <div class="project-tags">
                            <span>Python</span>
                            <span>Scikit-learn</span>
                            <span>Pandas</span>
                            <span>Regression</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="btn">View Details</a>
                            <a href="https://github.com/veer25x" class="btn btn-outline" target="_blank">GitHub</a>
                        </div>
                    </div>
                </div>
                
                <div class="project-card" data-category="ml">
                    <div class="project-img">
                        <i class="fas fa-film"></i>
                    </div>
                    <div class="project-info">
                        <h3>Movie Recommendation System</h3>
                        <p>Content-based filtering system suggesting movies based on user preferences and viewing history.</p>
                        <div class="project-tags">
                            <span>Python</span>
                            <span>Cosine Similarity</span>
                            <span>Pandas</span>
                            <span>NLP</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="btn">View Details</a>
                            <a href="https://github.com/veer25x" class="btn btn-outline" target="_blank">GitHub</a>
                        </div>
                    </div>
                </div>
                
                <div class="project-card" data-category="ml">
                    <div class="project-img">
                        <i class="fas fa-seedling"></i>
                    </div>
                    <div class="project-info">
                        <h3>Iris Species Classifier</h3>
                        <p>Classification model identifying iris flower species with high accuracy using ML algorithms.</p>
                        <div class="project-tags">
                            <span>Python</span>
                            <span>Classification</span>
                            <span>Scikit-learn</span>
                            <span>Matplotlib</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="btn">View Details</a>
                            <a href="https://github.com/veer25x" class="btn btn-outline" target="_blank">GitHub</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience & Education Section -->
    <section id="experience">
        <div class="container">
            <h2 class="section-title">Experience & Education</h2>
            <P>
                <h4>I have done some virtual internship</h4>
                curently i am learning and hope to attach more informatin.
            </P>
    <h2> Thank you </h2>
