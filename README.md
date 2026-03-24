# 📄 Professional Django Resume Builder

A full-stack, professional-grade online resume builder designed for developers and academics. This application provides a seamless, split-screen Live Preview experience, allowing users to craft stunning, ATS-friendly PDF resumes dynamically.

## ✨ Features
- **Live Split-Screen Preview:** Watch your PDF format update in real-time as you type, without ever reloading the page.
- **Auto-Save Cloud Engine:** Edits are silently and securely saved to the database via auto-debounced AJAX requests.
- **Drag-and-Drop Reordering:** Reorder your education, experience, skills, and projects effortlessly. 
- **Multiple Templates:** Instantly toggle between the rigorous "Academic (Classic)" style and the sleek "Modern Tech" styling.
- **ATS-Friendly PDF Export:** Uses the browser's native print engine to generate pristine, highlightable, 100% machine-readable PDFs.
- **Secure Authentication:** Integrated user login and registration securely isolates and protects private resume data.

## 🛠️ Tech Stack
- **Backend:** Python, Django (ORM, Authentication, Middleware Security)
- **Frontend:** HTML5, Tailwind CSS (via CDN), Vanilla JavaScript
- **Database:** SQLite (Default, scalable to PostgreSQL)
- **Libraries:** SortableJS

## 🚀 Quick Start

### 1. Requirements
- Python 3.8+

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone <your-repo-link>
cd Online_Resume_Builder_Using_Django
pip install -r requirements.txt
```

### 3. Database Setup
Navigate to the `core` application directory and execute the Django migrations to map the SQL tables:
```bash
cd core
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Local Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/register/` to create your first account and start building your resume!

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 📝 Copyright
© 2026 Shaik Mohammad Rafi. All Rights Reserved.
