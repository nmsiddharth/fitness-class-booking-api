#  Fitness Class Booking API

This is a Django REST API that allows users to:

- View all available fitness classes
- Book a class if slots are available
- Retrieve bookings based on client email

---

##  Tech Stack

- Python 3.10+
- Django 4+
- Django REST Framework
- SQLite3 (Default DB)

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone "https://github.com/your-username/fitness-class-api.git"
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv "venv"
"venv\Scripts\activate"  # Windows
```

### 3. Install Dependencies

```bash
pip freeze > "requirements.txt"
```


### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Load Sample Seed Data

path: fitness-class-booking-api/booking/fixtures/seed_data.json

```bash
python manage.py loaddata seed_data
```


### 6. Run Development Server

```bash
python manage.py runserver
```

Server will run at: `http://127.0.0.1:8000/`

---

##  API Endpoints

### 1. View All Upcoming Classes

**GET** `/classes/`

**Sample Request (Postman or cURL)**:

```bash
 GET: "http://127.0.0.1:8000/classes/"
```

**Sample Response**:

```json
[
  {
    "id": 1,
    "name": "Yoga",
    "start_time": "2025-07-26T10:00:00Z",
    "instructor": "Alice",
    "available_slots": 8
  }
]
```

---

### 2. Book a Class

**POST** `/book/`

**Body (JSON)**:

```json
{
  "fitness_class": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
```

**Sample Request**:

```bash
POST: "http://127.0.0.1:8000/book/" 
-Header: "Content-Type: application/json" 
-Body: "{
            "fitness_class": 1, 
            "client_name": "John Doe", 
            "client_email": "john@example.com"
        }"
```

**Validation Handled**:
- Ensures slots are available
- Prevents duplicate booking for the same email and class

---

### 3. View Bookings for a Client through specific email address

**GET** `/bookings/?client_email=john@example.com`

**Sample Request**:

```bash
GET: "http://127.0.0.1:8000/bookings/?client_email=john@example.com"
```

**Sample Response**:

```json
[
  {
    "id": 1,
    "fitness_class": 1,
    "client_name": "John Doe",
    "client_email": "john@example.com"
  }
]
```

---

##  Features

- Input validation using Django REST serializers
- Overbooking and duplicate booking prevention
- Clean and modular code structure (models, views, serializers)
- Easy to test with Postman or cURL

---

