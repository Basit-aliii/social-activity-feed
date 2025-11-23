# Social Activity Feed Backend

This is a FastAPI backend for a social activity feed system with the following features:

- User Signup/Login (JWT authentication)
- Create, Like, Follow, Block posts/users
- Activity feed showing:
  - "ABC made a post"
  - "DEF followed ABC"
  - "PQR liked ABC's post"
  - Admin/Owner deletions
- Admin and Owner permissions

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy (async) + SQLite
- JWT authentication
- Passlib for password hashing

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/Basit-aliii/social-activity-feed.git
cd social-activity-feed
Create and activate virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the server:

bash
Copy code
uvicorn app.main:app --reload
Open Swagger docs to test API:

arduino
Copy code
http://127.0.0.1:8000/docs
Project Structure
css
Copy code
activity-feed-backend/
├─ app/
│  ├─ main.py
│  ├─ db.py
│  ├─ models/
│  ├─ schemas/
│  ├─ routers/
│  └─ utils/
├─ venv/
├─ .gitignore
└─ README.md
Notes
Database tables are created automatically on startup.

Blocked users cannot see each other’s posts.

Admin and Owner can delete posts/users and manage permissions.