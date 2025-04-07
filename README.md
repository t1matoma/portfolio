#  Personal Portfolio Website

[![Django Version](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)

A professional portfolio website built with Django to showcase projects and provide contact information. Features an admin panel for easy content management.


##  Key Features
- **Project Gallery** - Display projects with descriptions and images
- **Contact Form** - Easy communication for potential clients
- **Admin Dashboard** - Add/edit projects without coding
- **Responsive Design** - Works on all devices
- **Light/Dark Mode** - (если есть, добавьте)

##  Tech Stack
| Category       | Technologies                         |
|----------------|--------------------------------------|
| Backend        | Django 4.2+, Python 3.10+           |
| Frontend       | HTML5, CSS3                          |
| Database       | SQLite (Production: PostgreSQL)      |

##  Quick Setup

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/portfolio.git
cd portfolio

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
```
##  Environment Configuration

The project uses environment variables for sensitive settings. 
**Never commit your `.env` file to version control!**

### Required `.env` variables:
```ini
# Django
SECRET_KEY=your-secret-key-here
```
Now you can open the site in your browser at `http://127.0.0.1:8000/`.
