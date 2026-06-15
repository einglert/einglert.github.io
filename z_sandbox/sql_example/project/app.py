from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def query_db(lastname):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE last_name = ?", (lastname,))
    results = cursor.fetchall()

    conn.close()
    return results

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/search', methods=['POST'])
def search():
    lastname = request.form['lastname']
    results = query_db(lastname)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
