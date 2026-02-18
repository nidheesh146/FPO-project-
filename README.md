FPO Service Management System 


Tech Stack:
Backend: Django + Django REST Framework,
Database: PostgreSQL,
Authentication: JWT,
Postman for testing



clone repo:
git clone https://github.com/nidheesh146/FPO-project-.git ,
cd FPO-project-


create environment:
python -m venv venv,
venv\Scripts\activate



Environment Variables:
SECRET_KEY=your-secret-key,,
DEBUG=True,
DB_NAME=your_database_name,
DB_USER=your_database_user,
DB_PASSWORD=your_database_password,
DB_HOST=localhost,
DB_PORT=5432


Run Migrations:
python manage.py makemigrations, 
python manage.py migrate


Create Superuser:
python manage.py createsuperuser

Run Server:
python manage.py runserver


To get jwt token:
POST /api/token/



Endpoints:

POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}


POST /api/token/refresh/
{
  "refresh": "your_refresh_token"
}


POST /api/service-requests/
{
  "service_type": "Harvest"
}


PATCH /api/service-requests/{id}/assign_provider/
{
  "provider": 3
}


PATCH /api/service-requests/{id}/assign_assistant/
{
  "assistant": 4
}



Start Work
PATCH /api/service-requests/{id}/start/

provider token


Complete work
PATCH /api/service-requests/{id}/complete/

provider token