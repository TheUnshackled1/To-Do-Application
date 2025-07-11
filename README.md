✅ Django CRUD To-do-List Application
A clean and functional **CRUD To-Do List app** built using **Django 5.2.4** and **Bootstrap 5**. This project demonstrates practical Django fundamentals including models, forms, views, templates and styling integration — ideal for showcasing your Python web development skills.

🔍 Overview
<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/0d7f04e1-c9eb-461e-becb-472e5c5c787a" />


This project allows users to:

- ✅ **Create** new tasks using a form.
- 📋 **Read** and view all current tasks in a styled list.
- ✏️ **Update** existing tasks.
- ❌ **Delete** tasks with confirmation.
- 🎨 Front-end styled with Bootstrap 5.

## 📁 Code Structure

```
todo/
├── task/
│   ├── migrations/
│   ├── templates/
│   │   ├── tasks.html
│   │   ├── edit_Task.html
│   │   ├── delete_Task.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── todo/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
└── manage.py
```
---

## 🛠 Tech Stack

- **Python 3**
- **Django 5.2.4**
- **SQLite** (default database)
- **Bootstrap 5.3.7** (via CDN)

 🚀 Getting Started

1. Clone the repository
```bash
git clone https://github.com/your-username/django-task-crud.git
cd django-task-crud
```

2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. Install Django
```bash
pip install django
```

4. Run migrations and start server
```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the app.



💡 Project Highlights

- Uses `ModelForm` for quick form generation.
- CSRF protection and validation built-in.
- Reusable template structure and Bootstrap styling.
- Basic MVC logic handled in Django views.

 🧑‍💻 Author
Developed by **Tyrone** — a Python/Django developer passionate about clean code and functional apps.

If you're hiring, this project demonstrates:
- Practical understanding of Django architecture.
- Ability to integrate front-end with back-end.
- Clean implementation of core CRUD logic.

 📜 License

Open-source under the [MIT License](LICENSE).
