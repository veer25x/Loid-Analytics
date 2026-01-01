from flask import Flask, render_template, request, send_file, flash, redirect, url_for, jsonify
import json
import uuid
import os
from datetime import datetime
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict, Any
import logging
from functools import wraps

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024  # 16KB max form data
app.config['DATA_DIR'] = Path('data')
app.config['STATIC_DIR'] = Path('static')
app.config['CERTIFICATES_FILE'] = app.config['DATA_DIR'] / 'certificates.json'

# Ensure directories exist
app.config['DATA_DIR'].mkdir(exist_ok=True)
app.config['STATIC_DIR'].mkdir(exist_ok=True)

@dataclass
class Certificate:
    """Certificate data model"""
    id: str
    name: str
    course: str
    date: str
    issued_at: str = None
    
    def __post_init__(self):
        if not self.issued_at:
            self.issued_at = datetime.now().isoformat()

class CertificateService:
    """Service for handling certificate operations"""
    
    def __init__(self, data_file: Path):
        self.data_file = data_file
        self._ensure_data_file()
    
    def _ensure_data_file(self) -> None:
        """Create data file if it doesn't exist"""
        if not self.data_file.exists():
            with open(self.data_file, 'w') as f:
                json.dump([], f)
    
    def load_certificates(self) -> List[Dict[str, Any]]:
        """Load all certificates from file"""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logger.error(f"Error loading certificates: {e}")
            return []
    
    def save_certificates(self, certificates: List[Dict[str, Any]]) -> None:
        """Save certificates to file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(certificates, f, indent=2, default=str)
        except IOError as e:
            logger.error(f"Error saving certificates: {e}")
            raise
    
    def add_certificate(self, certificate: Certificate) -> bool:
        """Add a new certificate"""
        try:
            certificates = self.load_certificates()
            certificates.append(asdict(certificate))
            self.save_certificates(certificates)
            logger.info(f"Certificate {certificate.id} added for {certificate.name}")
            return True
        except Exception as e:
            logger.error(f"Error adding certificate: {e}")
            return False
    
    def find_certificate(self, cert_id: str = None, name: str = None, course: str = None) -> Optional[Dict[str, Any]]:
        """Find a certificate by ID, name, or course"""
        certificates = self.load_certificates()
        
        if cert_id:
            return next((c for c in certificates if c.get('id') == cert_id), None)
        elif name and course:
            return next((c for c in certificates 
                        if c.get('name', '').lower() == name.lower() 
                        and c.get('course', '').lower() == course.lower()), None)
        return None

# Initialize services
cert_service = CertificateService(app.config['CERTIFICATES_FILE'])

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/internships')
def internships():
    return render_template('internships.html')

@app.route('/certificate', methods=['GET', 'POST'])
def certificate():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        course = request.form.get('course', '').strip()
        
        # Basic input validation
        if not name or not course:
            flash('Please fill in all required fields.', 'error')
            return render_template('certificate.html')
        
        if len(name) > 100 or len(course) > 200:
            flash('Input too long. Please shorten your text.', 'error')
            return render_template('certificate.html')
        
        # Generate certificate
        cert_id = str(uuid.uuid4())[:8].upper()
        date = datetime.now().strftime("%d-%m-%Y")
        
        certificate_obj = Certificate(
            id=cert_id,
            name=name,
            course=course,
            date=date
        )
        
        # Save to database
        if cert_service.add_certificate(certificate_obj):
            flash(f'Certificate generated successfully! Your ID: {cert_id}', 'success')
            # In a real app, you'd generate PDF here
            return redirect(url_for('certificate'))
        else:
            flash('Error saving certificate. Please try again.', 'error')
    
    return render_template('certificate.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    result = None
    if request.method == 'POST':
        cert_id = request.form.get('cert_id', '').strip().upper()
        name = request.form.get('name', '').strip()
        course = request.form.get('course', '').strip()
        
        if cert_id:
            found = cert_service.find_certificate(cert_id=cert_id)
        elif name and course:
            found = cert_service.find_certificate(name=name, course=course)
        else:
            flash('Please provide either Certificate ID or both Name and Course.', 'error')
            return render_template('verify.html')
        
        if found:
            result = {
                'status': 'verified',
                'certificate': found,
                'message': 'Certificate verified successfully!'
            }
            flash('Certificate found and verified!', 'success')
        else:
            result = {
                'status': 'not_found',
                'message': 'Certificate not found. Please check your details.'
            }
            flash('Certificate not found.', 'error')
    
    return render_template('verify.html', result=result)

@app.route('/verify/<cert_id>')
def verify_direct(cert_id):
    """Direct verification via URL"""
    found = cert_service.find_certificate(cert_id=cert_id.upper())
    
    if not found:
        flash('Certificate not found.', 'error')
        return redirect(url_for('verify'))
    
    result = {
        'status': 'verified',
        'certificate': found,
        'message': 'Certificate verified successfully!'
    }
    
    return render_template('verify.html', result=result)

@app.route('/api/certificates')
def api_certificates():
    """API endpoint to get all certificates (for demo)"""
    certificates = cert_service.load_certificates()
    return jsonify(certificates)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'certificates_count': len(cert_service.load_certificates())
    })

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Server error: {error}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Production configuration
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    
    app.run(host=host, port=port, debug=debug_mode)
    
    import hashlib
from functools import wraps

# Admin credentials (in production, use database with hashed passwords)
ADMIN_CREDENTIALS = {
    'admin': {
        'password': 'admin123',  # In production, use hashed passwords
        'name': 'System Administrator',
        'email': 'admin@loidanalytics.com'
    }
}

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()
 


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_logged_in' not in session:
            flash('Please log in to access the admin panel.', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in ADMIN_CREDENTIALS and password == ADMIN_CREDENTIALS[username]['password']:
            session['admin_logged_in'] = True
            session['admin_username'] = username
            session['admin_name'] = ADMIN_CREDENTIALS[username]['name']
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Get statistics
    certificates = cert_service.load_certificates()
    
    # Generate demo data for the dashboard
    stats = {
        'total_certificates': len(certificates),
        'certificates_growth': 15,  # demo data
        'total_courses': 6,
        'courses_growth': 8,
        'total_internships': 6,
        'internships_growth': 12,
        'verification_rate': 99.8,
        'total_verifications': len(certificates) * 3  # demo data
    }
    
    # Recent activity demo data
    recent_activity = [
        {
            'time': '10:30 AM',
            'date': 'Today',
            'user': 'Alex Johnson',
            'user_email': 'alex@example.com',
            'type': 'Certificate Generation',
            'type_icon': 'fas fa-certificate',
            'type_color': 'bg-gradient-to-r from-primary-500 to-cyan-500',
            'details': 'Generated certificate for Python Programming',
            'certificate_id': 'LA-2024-ABC12',
            'status': 'Completed',
            'status_color': 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400'
        },
        {
            'time': '09:15 AM',
            'date': 'Today',
            'user': 'Sarah Miller',
            'user_email': 'sarah@example.com',
            'type': 'Certificate Verification',
            'type_icon': 'fas fa-shield-alt',
            'type_color': 'bg-gradient-to-r from-green-500 to-emerald-500',
            'details': 'Verified certificate authenticity',
            'certificate_id': 'LA-2024-XYZ34',
            'status': 'Verified',
            'status_color': 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400'
        },
        {
            'time': 'Yesterday',
            'date': '3:45 PM',
            'user': 'Michael Chen',
            'user_email': 'michael@example.com',
            'type': 'Course Enrollment',
            'type_icon': 'fas fa-graduation-cap',
            'type_color': 'bg-gradient-to-r from-purple-500 to-pink-500',
            'details': 'Enrolled in Machine Learning Fundamentals',
            'certificate_id': None,
            'status': 'Completed',
            'status_color': 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400'
        }
    ]
    
    # Enhanced certificate data for admin
    enhanced_certificates = []
    for cert in certificates[-10:]:  # Show last 10 certificates
        enhanced_cert = cert.copy()
        enhanced_cert['status'] = 'active'
        enhanced_cert['verified_count'] = 3  # demo data
        enhanced_cert['email'] = 'user@example.com'  # demo data
        enhanced_cert['type'] = 'Course' if 'internship' not in cert['course'].lower() else 'Internship'
        enhanced_certificates.append(enhanced_cert)
    
    # Demo courses data
    courses = [
        {
            'id': 1,
            'name': 'Python Programming Mastery',
            'category': 'Programming',
            'difficulty': 'Beginner',
            'difficulty_color': 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400',
            'description': 'Master Python from basics to advanced concepts.',
            'enrollments': 1250,
            'price': 89,
            'gradient': 'from-blue-500 to-cyan-500'
        },
        {
            'id': 2,
            'name': 'Machine Learning Fundamentals',
            'category': 'AI/ML',
            'difficulty': 'Intermediate',
            'difficulty_color': 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
            'description': 'Learn ML algorithms and practical implementations.',
            'enrollments': 890,
            'price': 149,
            'gradient': 'from-purple-500 to-pink-500'
        },
        {
            'id': 3,
            'name': 'Data Science & Analytics',
            'category': 'Analytics',
            'difficulty': 'Intermediate',
            'difficulty_color': 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400',
            'description': 'Complete data analysis and visualization course.',
            'enrollments': 720,
            'price': 129,
            'gradient': 'from-green-500 to-teal-500'
        }
    ]
    
    # Demo internships data
    internships = [
        {
            'id': 1,
            'position': 'Python Development Intern',
            'company': 'TechCorp Solutions',
            'location': 'Remote',
            'type': 'Remote',
            'type_color': 'bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400',
            'description': 'Build and maintain Python applications and APIs.',
            'skills': ['Python', 'APIs', 'Backend'],
            'duration': '3-6 months',
            'stipend': '$2,500/month',
            'applications': 45
        },
        {
            'id': 2,
            'position': 'Machine Learning Intern',
            'company': 'AI Innovations Inc.',
            'location': 'San Francisco, CA',
            'type': 'On-site',
            'type_color': 'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400',
            'description': 'Develop ML models and work with large datasets.',
            'skills': ['ML', 'TensorFlow', 'Neural Networks'],
            'duration': '4-8 months',
            'stipend': '$3,000/month',
            'applications': 68
        }
    ]
    
    # Demo users data
    users = [
        {
            'id': 'USR001',
            'name': 'Alex Johnson',
            'email': 'alex@example.com',
            'phone': '+1 (555) 123-4567',
            'role': 'Student',
            'role_color': 'bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400',
            'joined_date': '2024-01-15',
            'certificates_count': 2,
            'status': 'active'
        },
        {
            'id': 'USR002',
            'name': 'Sarah Miller',
            'email': 'sarah@example.com',
            'phone': '+1 (555) 987-6543',
            'role': 'Instructor',
            'role_color': 'bg-purple-100 text-purple-800 dark:bg-purple-900/30 dark:text-purple-400',
            'joined_date': '2024-02-20',
            'certificates_count': 5,
            'status': 'active'
        }
    ]
    
    return render_template('admin.html',
                         stats=stats,
                         recent_activity=recent_activity,
                         certificates=enhanced_certificates,
                         courses=courses,
                         internships=internships,
                         users=users)

# Admin API endpoints
@app.route('/admin/api/certificates', methods=['GET', 'POST', 'DELETE'])
@login_required
def admin_api_certificates():
    if request.method == 'GET':
        certificates = cert_service.load_certificates()
        return jsonify(certificates)
    
    elif request.method == 'POST':
        data = request.json
        # Add new certificate logic
        return jsonify({'status': 'success', 'message': 'Certificate added'})
    
    elif request.method == 'DELETE':
        cert_id = request.args.get('id')
        # Delete certificate logic
        return jsonify({'status': 'success', 'message': 'Certificate deleted'})

@app.route('/admin/api/statistics')
@login_required
def admin_api_statistics():
    certificates = cert_service.load_certificates()
    
    # Calculate monthly growth
    monthly_data = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        'certificates': [65, 78, 90, 85, 120, 150, 180, 200, 220, 240, 260, 280]
    }
    
    return jsonify({
        'total_certificates': len(certificates),
        'monthly_growth': monthly_data,
        'popular_courses': [
            {'name': 'Python', 'value': 35},
            {'name': 'ML', 'value': 25},
            {'name': 'Data Science', 'value': 20},
            {'name': 'Deep Learning', 'value': 15},
            {'name': 'Business Analytics', 'value': 5}
        ]
    })
    import os

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'secure-password-here')



