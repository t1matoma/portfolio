Project Description
This is a personal portfolio website designed to showcase my projects and provide a way to contact me. The project is built with Django for the backend, using HTML and CSS for the frontend. It uses a SQLite database to store project data. New projects can be easily added through the built-in Django admin panel.

## Features
- Display of personal projects with descriptions

- Contact section for communication

- Admin panel for managing and adding new projects


- Responsive layout

## Technologies Used
- Python (Django)

- HTML

- CSS

- SQLite


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    ```

2. Navigate to the project directory:
    ```bash
    cd yourrepo
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On Mac/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run migrations:
    ```bash
    python manage.py migrate
    ```

7. Start the development server:
    ```bash
    python manage.py runserver
    ```

Now you can open the site in your browser at `http://127.0.0.1:8000/`.
