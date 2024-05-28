from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# Define the model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    identity_id = db.Column(db.String(50), nullable=False)


# Create the database
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        mobile_number = request.form['mobile_number']
        email = request.form['email']
        identity_id = request.form['identity_id']
        image_file = request.files['image']
        if image_file:
            filename = secure_filename(image_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)

            new_user = User(name=name, mobile_number=mobile_number, email=email, image=filename,
                            identity_id=identity_id)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!')
            return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.mobile_number = request.form['mobile_number']
        user.email = request.form['email']
        user.identity_id = request.form['identity_id']
        image_file = request.files['image']
        if image_file:
            filename = secure_filename(image_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(filepath)
            user.image = filename

        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('index'))

    return render_template('edit.html', user=user)


@app.route('/delete/<int:id>')
def delete(id):
    user = User.query.get_or_404(id)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], user.image)
    if user.image and os.path.exists(image_path):
        os.remove(image_path)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
