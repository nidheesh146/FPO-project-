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

Create Service Request
POST /api/service-requests/

Assign Provider
PATCH /api/service-requests/{id}/

Assign Assistant
PATCH /api/service-requests/{id}/

Update Status
PATCH /api/service-requests/{id}/

Get Request
GET /api/service-requests/{id}/


POSTMAN Collection is in project root
