# Library Project

This project is a Django-based library management system with the following technologies:
- **Django**
- **PostgreSQL**
- **HTML/CSS**
- **Bootstrap**

## Features
The project allows users to:
- Register
- View books and their authors
- Create a new author
- View the list of registered users
- Add a book as an order and delete it
- You can also search for books by filtering 

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yurakomarnitskyi/Library-project
    cd library-project
    ```

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

Run the Django application:

```bash
python manage.py runserver
docker-compose -p library up
```
## API Endpoint 
# User Management:
```http://127.0.0.1:8000/api/user/
   http://127.0.0.1:8000/api/user/1/
``` GET user 
```http://127.0.0.1:8000/api/user/1/``` PUT change user info
```http://127.0.0.1:8000/api/user/```  POST create user
```http://127.0.0.1:8000/api/user/50/``` DELETE user method
# Author Management:
```http://127.0.0.1:8000/api/author/``` GET author 
```http://127.0.0.1:8000/api/author/``` POST add new author
```http://127.0.0.1:8000/api/author/38/``` PUT change author info 
```http://127.0.0.1:8000/api/author/38/``` DELETE author
# Book Management
```http://127.0.0.1:8000/api/book/``` GET book 
```http://127.0.0.1:8000/api/book/``` POST add new book
```http://127.0.0.1:8000/api/book/38/``` PUT change book info 
```http://127.0.0.1:8000/api/book/38/``` DELETE book
# Order Management
```http://127.0.0.1:8000/api/order/``` GET order
```http://127.0.0.1:8000/api/order/``` POST add new order
```http://127.0.0.1:8000/api/order/38/``` DELETE order




