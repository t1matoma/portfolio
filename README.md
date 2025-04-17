#  Personal Portfolio Website

[![Django Version](https://img.shields.io/badge/Django-5.1+-green.svg)](https://www.djangoproject.com/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)

A professional portfolio website built with Django to showcase projects and provide contact information. Features an admin panel for easy content management.


##  Key Features
- **Project Gallery** - Display projects with descriptions and images
- **Contact Form** - Easy communication for potential clients
- **Admin Dashboard** - Add/edit projects without coding
- **Responsive Design** - Works on all devices

##  Tech Stack
| Category       | Technologies                         |
|----------------|--------------------------------------|
| Backend        | Django 5.1+, Python 3.10+            |
| Frontend       | HTML5, CSS3                          |
| Database       | SQLite                               |

## Quick Start with Docker


### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/portfolio.git
cd portfolio
```
###  Environment Configuration

The project uses environment variables for sensitive settings. 
**Never commit your `.env` file to version control!**

### Required `.env` variables:
```ini
# Django
SECRET_KEY=your-secret-key-here
```

To start the application with Docker, you can use the provided script `run.sh`, which will:

- Build the Docker image.
- Apply migrations.
- Collect static files.
- Start the server.

### Steps to run the server:

1. Ensure Docker and Docker Compose are installed on your machine.
2. Run the following command to start the application:

```bash
   chmod +x run.sh
   ./run.sh
```

Now you can open the site in your browser at `http://127.0.0.1:8000/`.


### Creating a Superuser

```bash
docker-compose up -d
```

```bash
docker-compose exec django python portfolio/manage.py createsuperuser
```
### Access the Admin Panel

Once the server is running, you can access the Django admin panel at:

http://127.0.0.1:8000/admin/



##  Quick Setup without Docker

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone repository
git clone https://github.com/t1matoma/portfolio.git
cd portfolio

# 2. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows

# 3. Install dependencies
pip3 install -r requirements.txt

# 5. Run migrations
cd portfolio
python3 manage.py migrate

# 6. Create admin user
python3 manage.py createsuperuser

# 7. Run development server
python3 manage.py runserver
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

