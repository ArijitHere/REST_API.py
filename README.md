# 🐍 Pure Python REST API (No Flask Required)

A simple REST-like API built using Python's built-in `http.server` module.  
This API supports **GET, POST, PUT, DELETE** operations for managing user data — all in-memory, without any external dependencies.

---

## 📌 Features
- **GET /users** → Fetch all users  
- **GET /users/{id}** → Fetch a single user by ID  
- **POST /users** → Create a new user  
- **PUT /users/{id}** → Update an existing user  
- **DELETE /users/{id}** → Remove a user  
- Works **without installing Flask** or any third-party library  
- Runs **anywhere** Python is available  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/pure-python-rest-api.git
cd pure-python-rest-api

2️⃣ Run the Server
python main.py

3.Get all users
curl -X GET http://localhost:5000/users

4.Create a new user
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "Alice", "email": "alice@example.com"}'

5.Update a user
curl -X PUT http://localhost:5000/users/1 \
-H "Content-Type: application/json" \
-d '{"name": "Updated Name"}'

6.curl -X DELETE http://localhost:5000/users/1


