from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = 'bug_tracker.db'

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bugs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        severity TEXT,
        status TEXT,
        created_at TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM bugs")
    bugs = c.fetchall()
    conn.close()
    return render_template('index.html', bugs=bugs)

@app.route('/add', methods=['GET', 'POST'])
def add_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        severity = request.form['severity']
        status = request.form['status']
        created_at = request.form['created_at']
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("INSERT INTO bugs (title, description, severity, status, created_at) VALUES (?, ?, ?, ?, ?)",
                  (title, description, severity, status, created_at))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_bug.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
