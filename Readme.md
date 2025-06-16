# 🦸‍♀️ Superheroes API

A simple Flask API that allows users to explore superheroes, view their powers, and assign powers with varying strength levels.

---

## 📦 Technologies Used

- Python  
- Flask  
- Flask-SQLAlchemy  
- Flask-Migrate  
- SQLite  
- Postman (for API testing)

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd superheroes-api
```

### 2. Create and Activate a Virtual Environment
```bash
pipenv install
pipenv shell
```

### 3. Initialize and Run the Application
```bash
cd server
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Seed the Database
```bash
python seed.py
```

---

## 📁 Project Structure

```
superheroes-api/
├── Pipfile
├── Pipfile.lock
├── README.md
└── server/
    ├── app.py
    ├── models.py
    ├── seed.py
    ├── instance/
    │   └── superheroes.db
    ├── migrations/
    │   ├── env.py
    │   ├── script.py.mako
    │   ├── README
    │   ├── alembic.ini
    │   └── versions/
    │       └── <migration_file>.py
    └── __pycache__/
```

---

## 📋 API Endpoints

### GET `/`
Returns a welcome message.  
Example Response:
```json
{ "message": "Welcome to the Superheroes API!" }
```

### GET `/heroes`
Returns a list of all heroes.

### GET `/heroes/<id>`
Returns a single hero with their associated powers.

### GET `/powers`
Returns a list of all powers.

### GET `/powers/<id>`
Returns a specific power and all associated heroes.

### PATCH `/powers/<id>`
Updates the description of a power.  
**Validation**: Description must be at least 20 characters long.

### POST `/hero_powers`
Assigns a power to a hero with a specified strength.  
**Valid strengths**: `"Strong"`, `"Average"`, `"Weak"`

---

## 📫 Author

**Emmanuel Njung'e**  
