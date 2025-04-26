# goit-pythonweb-hw-08

Створення REST API для управління контактами.
Використано FastAPI, SQLAlchemy, PostgreSQL.

## Функціонал

- CRUD-операції з контактами
- Пошук за іменем, прізвищем або email
- Отримання контактів з днями народження на найближчі 7 днів

## Технології

- Python 3.12+
- FastAPI
- PostgreSQL (через Docker)
- SQLAlchemy
- Pydantic
- Uvicorn

## Запуск проєкту

1. Створити контейнер PostgreSQL:

docker run --name contacts-db -p 5433:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 -e POSTGRES_DB=contacts -d postgres


2. Створити файл `.env`:

DB_USER=postgres DB_PASSWORD=12345 DB_HOST=localhost DB_PORT=5433 DB_NAME=contacts


3. Встановити залежності:

pip install -r requirements.txt


4. Ініціалізувати базу:

python src/init_db.py


5. Запустити сервер:

uvicorn src.main:app --reload


## Swagger

Документація: http://127.0.0.1:8000/docs

## Приклад POST-запиту

POST /contacts/

{ "first_name": "Anna", "last_name": "Ivanova", "email": "anna@example.com", "phone": "0501234567", "birthday": "1990-04-22", "extra_info": "Колега" }

## Налаштування середовища

1. Створіть файл `.env` на основі `.example.env`
2. Вкажіть у ньому ваші параметри підключення до бази:

DB_USER=postgres  
DB_PASSWORD=12345  
DB_HOST=localhost  
DB_PORT=5433  
DB_NAME=contacts
