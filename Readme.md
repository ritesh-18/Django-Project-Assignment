# 🌟 All Items Project

## 📖 Project Overview
The **"All Items"** project is a simple web application designed to manage a list of items. It displays item details in a table format and allows users to perform CRUD operations. If no items are available, it displays an appropriate message. The project leverages **Django** for server-side processing and dynamic content rendering.

---

## ✨ Features
- 📝 Display a list of items with their details.
- ➕ Add new items.
- ✏️ Update existing items.
- ❌ Delete items.
- ✅ Validation for item data (e.g., ensuring the date of birth is not in the future).

---

## 🛠️ Technologies Used
- **Django**: A high-level Python web framework for building web applications.
- **SQLite**: A lightweight database for storing item data.

---

## ⚙️ Prerequisites
- ✅ Python installed on your machine.
- ✅ Django installed in your Python environment (`pip install django`).
- ✅ Basic knowledge of HTML, CSS, and Django.

### 🚀 For Server-Side Rendering:
Use tools like **Thunder Client** or **Postman** for performing CRUD operations.

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
Clone the project repository to your local machine:
```bash
git clone <repository-url>
cd projectCRUD



 SetUp the DataBase
```bash
python manage.py makemigrations
python manage.py migrate


## Run the Development Server
```bash
python manage.py runserver


projectCRUD/
│
├── crud/
│   ├── migrations/
│   ├── templates/
│   │   ├── delete_item.html
│   │   ├── index.html
│   │   ├── item_list.html
│   │   └── update_item.html
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── projectCRUD/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
└── README.md
