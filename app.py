from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('Temp.db')
    c = conn.cursor()
    c.execute('select * from weatherdata')
    data = c.fetchall()
    return render_template('table.html', data=data)


if __name__ == '__main__':
    app.run()
