from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM user').fetchall()
    conn.close()
    return render_template('index.html', users=users)


@app.route('/new', methods=["GET", "POST"])
def new():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_db_connection()
        conn.execute('INSERT into user(name, email) VALUES(?, ?)', (name, email))
        conn.commit()

    return render_template('new.html')


if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
