🚀 Backend Engineer Portfolio | Mayank Gupta
A clean, high-performance personal portfolio focused on backend architecture. Built with Django 4.2 and Bootstrap 5, this project prioritizes speed, security, and a professional recruiter-friendly interface.(use ai for frontend development)

🔗 Live Link
View the portfolio here: https://mayankgupta.pythonanywhere.com

🏗️ Technical Architecture
This project follows a modular Django structure, separating the landing experience from the technical showcase:

portfolio/: Project configuration, security settings, and global routing.

core/: Manages the Home and About pages, profile bio, and skill badges.

projects/: A dedicated app for the dynamic project gallery. It supports auto-playing muted video demos and technical stack tagging.

templates/: Global base templates using a base.html + includes/ strategy for DRY (Don't Repeat Yourself) code.

Key Backend Decisions
Static & Media Handling: Uses Whitenoise for efficient static file serving in production.

Admin-Driven Content: All project details, videos, and thumbnails are managed via the Django Admin—no hardcoding in HTML.

Performance: Optimized with lazy-loading posters for videos and a lightweight Bootstrap 5 CDN integration.

🛠️ Tech Stack
Framework: Django 4.2 (MVT Architecture)

Frontend: Bootstrap 5 (Responsive Grid & Cards)

Database: SQLite (Default for portability)

Deployment: PythonAnywhere with WSGI & Virtualenv

Security: Environment variables for SECRET_KEY and DEBUG states.

⚙️ Local Setup & Installation
Clone the Repository:

Bash
git clone https://github.com/mayankgupta-24/my-portfolio.git <br>
cd my-portfolio

Initialize Virtual Environment:
Bash
python -m venv env <br>
Windows: env\Scripts\activate | Mac/Linux: source env/bin/activate

Install Dependencies:
Bash
pip install -r requirements.txt

Code snippet
DEBUG = True <br>
SECRET_KEY = your-local-dev-key <br>
Database Setup: Default

Bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

📁 Project Highlights <br>
Auto-play Video Demos: Projects feature muted, looping video previews with image posters to prevent layout shift during loading.

Skill Badges: Categorized backend skills with hover-lift effects for better interactivity.

Production Ready: Configured with ALLOWED_HOSTS, STATIC_ROOT, and secure WSGI entry points.

👤 Contact & Links
GitHub: mayankgupta-24

LinkedIn: https://www.linkedin.com/in/mayank-gupta-4259a8240

Email: btwitsmayank24@gmail.com
