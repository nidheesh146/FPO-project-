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

Register fpo
POST /auth/register-fpo/

{
  "username": "your_username",
  "password": "your_password",
  "name":"name"
}

register farmer
POST /auth/register/
{
  "username": "your_username",
  "password": "your_password"
}


Login for all roles:
POST /auth/login/

{
  "username": "your_username",
  "password": "your_password"
}
response:
{
  "access": "jwt_token",
  "refresh": "refresh_token"
}






FPO Creates Provider
POST /auth/create-provider/

Header:

Authorization: Bearer : "fpo_token"
{
  "username": "provider1",
  "password": "test123",
  "name": "Provider One"
}



Provider Creates Assistant

POST /auth/create-assistant/

Header:

Authorization: Bearer "provider_token"
{
  "username": "assistant1",
  "password": "test123",
  "name": "Assistant One"
}


Farmer Creates Service Request

POST /requests/

Authorization: Bearer "farmer_token"

{
  "service_type": "Harvesting"
}
status becomes pending

FPO Assigns Provider

PATCH /requests/<request_id>/assign-provider/


Header:

Authorization: Bearer <fpo_token>

body:
{
  "provider_id": 3
}

Status becomes ASSIGNED



Provider Accepts / Rejects:

PATCH /requests/<request_id>/respond/


Header:

Authorization: Bearer <provider_token>

Body:

{
  "action": "accept"
}

status becomes accepted


Provider Assigns Assistant:

PATCH /requests/<request_id>/assign-assistant/


Header:

Authorization: Bearer <provider_token>

Body:

{
  "assistant_id": 5
}


Assistant Starts Work:

PATCH /requests/<request_id>/start/

Header:

Authorization: Bearer <assistant_token>

status becomes IN PROGRESS


Assistant Completes Work:

PATCH /requests/<request_id>/complete/


Header:

Authorization: Bearer <assistant_token>

Staus becomes COMPLETED



FPO → View Providers:

GET /auth/providers/



Provider → View Assistants:

GET /auth/assistants/


View Request Details:

GET /requests/<request_id>/


PENDING → ASSIGNED → ACCEPTED → IN_PROGRESS → COMPLETED
