# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store tasks
tasks = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the task from the form
        task = request.form['task']
        # Add the task to the list
        tasks.append(task)
        # Redirect to the home page
        return redirect(url_for('index'))
    return render_template('index.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
