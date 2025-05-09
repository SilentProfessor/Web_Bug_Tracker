# Web_Bug_Tracker
Bug Tracker is a lightweight, web-based application that helps developers and QA teams efficiently log, track, and manage bugs or issues throughout the software development lifecycle. It offers a user-friendly interface to add, view, update, and delete bug reports with key attributes like severity, status, and timestamps. 
# Bug Tracker Web App

A simple and lightweight bug tracking system built using Python Flask, SQLite, and Bootstrap. This application allows developers and testers to log, view, update, and delete bug reports in a web interface.

---

## Features

- Add new bug reports (title, description, severity, status, timestamp)
- View all reported bugs in a sortable table
- Edit and update existing bugs
- Delete resolved or invalid bugs
- Clean and responsive Bootstrap-based UI
- Persistent storage using SQLite
- Lightweight and easy to deploy

---

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Backend**: Python Flask
- **Database**: SQLite

---

## Getting Started

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/web_bug_tracker.git
cd web_bug_tracker

2. Install dependencies:

pip install flask

3. Run the application:

python app.py

4. Open in your browser:

http://127.0.0.1:5000

5. Project Structure
bug_tracker/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── index.html
│   ├── add_bug.html
│   └── edit_bug.html
├── static/                # CSS and assets
│   └── style.css
├── bug_tracker.db         # SQLite database (auto-created)
├── LICENSE                # MIT License
└── README.md              # Project documentation


---


