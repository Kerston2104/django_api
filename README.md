# Django API

This is a RESTful API built using **Django** and **Django REST Framework**. The project is designed to serve as a backend service, capable of handling authentication, CRUD operations, and scalable API endpoints for various applications.

---

## 🚀 Features

- 🔐 Token-based Authentication
- 📦 Modular App Structure
- 🔄 Full CRUD Support
- 🌐 CORS Enabled
- 📂 Environment-based Settings
- 🧪 Easy Testing Setup

---

## 🛠️ Tech Stack

- Python 3.x  
- Django  
- Django REST Framework  
- SQLite / PostgreSQL (configurable)  
- CORS Headers  
- DRF Simple JWT (optional for auth)  

---

## 📁 Project Structure

```
django_api/
├── ApiProject/                # Your core API app
├── ApiApplication/         # Main Django settings and URLs
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

---

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kerston2104/django_api.git
   cd django_api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   #For Linux & MAC:
   source venv/bin/activate
   # For Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 🧪 API Testing

Use tools like **Postman**, **Insomnia**, or **cURL** to test your endpoints.

- Base URL: `http://localhost:8000/`
- Common endpoints:
  - `/api/user/` (user add to the database)
  - `/admin/` (Django admin)

---

## ✨ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 🙌 Acknowledgements

Thanks to the Django and DRF communities for their amazing tools and documentation!
