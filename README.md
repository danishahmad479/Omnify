# Fitness Class Booking API

This is a Django REST API for a fitness studio that manages fitness classes and bookings.  
Clients can view upcoming classes, book a spot, and see their bookings.

---

## Features

- View upcoming fitness classes  
- Create new fitness classes (for admins)  
- Book a spot in a fitness class (if slots available)  
- Retrieve bookings by client email

---

## Tech Stack

- Python 3.x  
- Django & Django REST Framework  
- SQLite (default Django in-memory DB)

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/danishahmad479/Omnify.git
cd OMNIFY

2. **Create and activate a virtual environment** 


python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

4 . Run migrations

python manage.py makemigrations
python manage.py migrate


Sample Postman requests

GET /classes/

# Get all classes
curl -X GET http://localhost:8000/classes/

POST /classes/ with JSON body 

# Create a class
curl -X POST http://localhost:8000/classes/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Zumba","date_time":"2025-06-15T19:00:00Z","instructor":"Bob","total_slots":15,"available_slots":15}'


POST /book/ with JSON body 

# Book a class
curl -X POST http://localhost:8000/book/ \
  -H "Content-Type: application/json" \
  -d '{"fitness_class":1,"client_name":"John Doe","client_email":"john.doe@example.com"}'

GET /bookings/?email=john.doe@example.com

# Get bookings by email
curl -X GET "http://localhost:8000/bookings/?email=john.doe@example.com"


