# 🦸‍♀️ Superheroes API

Welcome to the **Superheroes API** — your backend command center for exploring legendary heroes, uncovering their awesome powers, and assigning epic strengths worthy of a cinematic universe.

---

## ⚙️ Powered By

This project is forged using:

- 🐍 Python  
- 🔥 Flask  
- 🧬 Flask-SQLAlchemy  
- 🧳 Flask-Migrate  
- 💾 SQLite  
- 🧪 Postman (for heroic testing)

---

## 🚀 Getting Started — Assemble!

Calling all dev-vengers! Follow these steps to bring your API to life:

### 1. Clone the Repository
```bash
git clone https://github.com/Emmanuel-Njunge/superheroes-api
cd superheroes-api
```

### 2. Create and Activate a Virtual Environment
```bash
pipenv install
pipenv shell
```

### 3. Fire Up the Server
```bash
cd server
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Summon Your Hero Roster
```bash
python seed.py
```

---

## 🗂️ Secret Lair Layout

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

## 🧭 API Endpoints

### GET `/`
Returns a welcome message.  
```json
{ "message": "Welcome to the Superheroes API!" }
```

### GET `/heroes`
Returns all registered heroes.

### GET `/heroes/<id>`
Shows a hero and all their mighty powers.

### GET `/powers`
Returns the full catalog of powers, from invisibility to laser eyes.

### GET `/powers/<id>`
Shows a specific power and the heroes who wield it.

### PATCH `/powers/<id>`
Update a power’s description.  
**Must be at least 20 characters long. Lol choose your words wisely.**

### POST `/hero_powers`
Assigns a power to a hero with a declared strength.  
**Valid strengths**: `"Strong"`, `"Average"`, `"Weak"` — even heroes have off days.

---

## 🧑‍🎤 Authored By

**Emmanuel Njung'e**  
GitHub: [Emmanuel-Njunge](https://github.com/Emmanuel-Njunge)

---


