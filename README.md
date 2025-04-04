﻿
# 📝 Flask To-Do List

A simple web-based to-do list built with Flask, Jinja, and Bootstrap.

## 🚀 Features

* Add, delete, and mark tasks as complete
* Responsive design with Bootstrap
* Lightweight and easy to set up

## 🛠️ Technologies Used

* **Flask** (Python)
* **Jinja** (Templating)
* **Bootstrap** (Styling)
* **SQLite** (Database)

## 📦 Installation

1. **Clone the repository** :

```bash
   git clone https://github.com/yourusername/flask-todo.git
   cd flask-todo
```

1. **Create a virtual environment** :

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

1. **Install dependencies** :

```bash
   pip install -r requirements.txt
```

1. **Run the application** :

```bash
   python app.py
```

1. Open your browser and go to `http://127.0.0.1:5000`

## 📂 Project Structure

```
flask-todo/
│── static/          # CSS, JS, images
│── templates/       # HTML templates (Jinja)
│── app.py           # Main Flask application
│── requirements.txt # Dependencies
│── README.md        # Project documentation
└── database.db      # SQLite database (auto-generated)
```

## 🛠️ Future Improvements

* User authentication
* Task categories & due dates
* Dark mode support
