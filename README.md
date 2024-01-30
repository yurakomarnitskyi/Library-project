# Library project

Django
PostgreSQl
HTML/CSS
Bootsraap

# Features
From the very beginning, this project allows the user to register. Then the user has the opportunity to see the books and their authors. It is possible to create a new author.
You can also view the list of registered users 
You can add a book as an order and delete it 
# Installation
Clone the repository:
git clone https://github.com/yurakomarnitskyi/Library-project
cd library-project

Create a virtual environment:

python -m venv venv
Activate the virtual environment:

source venv/bin/activate
Install the dependencies:

pip install -r requirements.txt
Usage
Run the Django application:
docker-compose -p library up
Open your web browser and navigate to http://localhost:8000

API Endpoints

# Auth System

This microservice provides JWT Authentication, managing user's favorites and product question.

## Features
- **Django:** 
- **PostgreSQL:** 
- **HTML/CSS:**
- **Bootstrap:**
From the very beginning, this project allows the user to register. Then the user has the opportunity to see the books and their authors. It is possible to create a new author.
You can also view the list of registered users 
You can add a book as an order and delete it 
## Installation

1. Clone the repository:
2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
   
## Usage

1. Run the Django application:

    ```bash
    python manage.py runserver
    ```
     ```bash
    docker-compose -p library up
    ```
    

2. Open your web browser and navigate to `http://localhost:8000`

## API Endpoints

- `/questions`: GET or POST User's questions

- `/favorites`: GET or POST User's favorite list
  
- `/auth/users/`: POST User's register
  
- `/auth/users/activation/`: POST User's activation account

- `/auth/jwt/create/`: POST Login user's and generates token

- `/auth/jwt/refresh/`: POST Refresh token

- `/auth/users/reset_password/`: POST Password reset request

- `/auth/users/reset_password_confirm/`: POST Confirm and set a new password

- `/auth/users/me/`: DELETE Account deletion
