# app.py
import matplotlib

matplotlib.use('Agg')  # Set the backend before importing pyplot
import matplotlib.pyplot as plt  # Import pyplot after setting the backend

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from io import BytesIO
import base64

app = Flask(__name__)


# Database initialization
def initialize_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, value INTEGER)''')
    conn.commit()
    conn.close()


initialize_database()


# Route to add data manually
@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        value = request.form['value']
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO data (value) VALUES (?)", (value,))
        conn.commit()
        conn.close()
        return redirect(url_for('display_data'))
    return render_template('add_data.html')


# Route to display data
@app.route('/')
def display_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT value FROM data")
    data = c.fetchall()
    conn.close()

    values = [row[0] for row in data]

    # Plotting data with data points labeled
    plt.figure()
    plt.plot(values)
    for i, value in enumerate(values):
        plt.text(i, value, str(value), ha='center', va='bottom')
    plt.title('Data Visualization')
    plt.xlabel('Data Points')
    plt.ylabel('Values')
    plt.grid(True)

    # Convert plot to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return render_template('index.html', plot_data=plot_data)


if __name__ == '__main__':
    app.run(debug=True)
