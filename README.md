# 📝 Django Blog Platform

A secure, feature-rich blog application built with **Django**, focusing on clean backend architecture, authentication, authorization, and modern UI/UX.

This project was designed and developed as a **production-oriented portfolio project**, not just a tutorial implementation.

---

## 🚀 Live Demo
> https://blogsite-pankaj.onrender.com/

---

## 🧰 Tech Stack

- **Backend:** Django
- **Authentication:** Django Auth System
- **Database:** SQLite (local) / PostgreSQL (production-ready)
- **Frontend:** HTML, CSS (Responsive, Mobile-first)
- **Deployment Ready:** Gunicorn + Render
- **Version Control:** Git & GitHub

---

## ✨ Features

### 📰 Blog System
- Blog listing with pagination
- SEO-friendly slug-based URLs
- Blog detail page with view counter
- Reading time estimation

### 👤 Authentication & Authorization
- Login / Logout system
- Public registration **disabled** (security-first decision)
- Admin-controlled user creation
- Password reset via email (configurable)

### ❤️ Engagement
- Like / Unlike system (one like per user)
- Comment system (logged-in users only)
- Users can delete **only their own comments**

### 🔐 Security Decisions
- Public signup disabled to reduce attack surface
- Auth-based permissions for all write actions
- CSRF protection enabled
- Environment variables used for secrets
- `.env` excluded from version control

### 🎨 UI / UX
- Responsive mobile-friendly layout
- Dark mode toggle with persistence
- Animated UI interactions
- Flash messages for user actions
- Clean navigation with dropdown & hamburger menu

---

## 🛡️ Why Registration Is Disabled

Public user registration was intentionally disabled to:
- Prevent abuse and spam
- Maintain strict control over user roles
- Demonstrate a **security-first mindset**

Users are created and managed via the Django Admin panel.

> Authentication without proper authorization is dangerous — this project prioritizes controlled access.

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository
```
git clone https://github.com/pankajmourya007/blogsite.git
cd blogsite
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Environment variables

Create a `.env` file (not committed):

```
SECRET_KEY=your-secret-key
DEBUG=True
```

### 5️⃣ Migrate & run

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📁 Project Structure (Simplified)

```
blogsite/
│── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
│── blogsite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│── static/
│── templates/
│── manage.py
```

---

## 📌 What I Learned

* Django project architecture & MVC flow
* Authentication vs Authorization
* Secure handling of POST actions
* Django templates best practices
* Real-world debugging & migration handling
* UI/UX improvements without JS frameworks
* Secure Git & deployment workflows

---

## 🧠 Interview Talking Point

> *“I intentionally disabled public registration to reduce attack surface and enforced strict authorization rules to ensure users can only modify their own data.”*

---

## 🔮 Future Improvements

* Email verification on signup
* Rate limiting for comments
* User profile pages
* Unit & integration tests
* Analytics dashboard
* Custom 404 / 500 pages

---

## 👨‍💻 Author

**Pankaj Mourya**
Cybersecurity & Backend Enthusiast
GitHub: [https://github.com/pankajmourya007](https://github.com/pankajmourya007)

---

⭐ If you like this project, feel free to star the repo!
