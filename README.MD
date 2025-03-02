# Django E-commerce Project

## Description
This is a Django-based ORGANIC food web application that allows users to browse products, add them to a cart, and complete their purchases. The project includes authentication, cart management, and order processing.

## Features
- User authentication (Sign up, Login, Logout)
- Product listing and details
- Shopping cart functionality
- Order management
- Admin panel for managing products and orders

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, can be changed to PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render

## Installation

### 1. Clone the Repository
```sh
 git clone https://github.com/cykoravish/organic-food-python.git
 cd organic_food_python
```

### 2. Create and Activate Virtual Environment
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
 pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
 python manage.py migrate
```

### 5. Create a Superuser
```sh
 python manage.py createsuperuser
```

### 6. Run the Development Server
```sh
 python manage.py runserver
```

The project will be accessible at `http://127.0.0.1:8000/`.

## Deployment on Render

1. Push your project to a GitHub repository.
2. Create a new Django web service on Render.
3. Add the environment variables (e.g., `SECRET_KEY`, `DEBUG=False`, database settings).
4. Run migrations using:
   ```sh
   python manage.py migrate
   ```
5. Restart the Render service if needed.

## Troubleshooting
- If you encounter `no such table: authcart_product`, try running:
  ```sh
  python manage.py makemigrations authcart
  python manage.py migrate authcart
  ```
- Check your database file exists: `ls /opt/render/project/src/db.sqlite3`
- Restart the service if needed.

## License
This project is open-source and available under the [MIT License](LICENSE).

---

