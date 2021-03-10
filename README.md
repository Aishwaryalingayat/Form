# Sample project

## Instructions

* ### Environment Set-up Instructions
  1. Set up a virtual environment
        ```bash
        pip install virtualenv
        virtualenv <env_name>
        source <env_name>/scripts/activate
        ```
  1. Install requirements
        ```bash
        pip install -r requirements.txt
        ```
  1. Migrate
        ```bash
        python manage.py migrate
        ```
  1. Run server
        ```bash
        python manage.py runserver
        ```
  1. Open in browser http://127.0.0.1:8000/