from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import (LoginManager, UserMixin, current_user, login_required,
                         login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))
db.create_all()


@app.route('/')
def home():
  return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == 'POST':
    new = User(
      email=request.form['email'], 
      name=request.form['name'], 
      password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
    )
    db.session.add(new)
    db.session.commit()
    return redirect(url_for('secrets', name=new.name))
  else:
    return render_template("register.html")


@app.route('/login')
def login():
  return render_template("login.html")


@app.route('/secrets')
def secrets():
  return render_template("secrets.html", name=request.args.get('name'))


@app.route('/logout')
def logout():
  pass


@app.route('/download')
def download():
  return send_from_directory(directory='static/files', filename='cheat_sheet.pdf')


if __name__ == "__main__":
  app.run(debug=True)
