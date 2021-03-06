from flask import (Flask, flash, redirect, render_template, request, send_from_directory, url_for)
from flask_login import (LoginManager, UserMixin, current_user, login_required, login_user, logout_user)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))
db.create_all()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


@app.route('/')
def home():
  return render_template("index.html", login=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == 'POST':
    user = User.query.filter_by(email=request.form['email']).first()
    if user:
      flash('An account has already been registered under this email, please log in instead.')
      return redirect(url_for('login'))
    else:
      new = User(
        email=request.form['email'], 
        name=request.form['name'], 
        password=generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
      )
      db.session.add(new)
      db.session.commit()
      login_user(new)
      return redirect(url_for('secrets'))
  else:
    return render_template("register.html", login=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    user = User.query.filter_by(email=request.form['email']).first()
    if not user:
      flash('A user with that email does not exist, please try again.')
      return redirect(url_for('login'))
    elif not check_password_hash(user.password, request.form['password']):
      flash('Incorrect password, please try again.')
      return redirect(url_for('login'))
    else:
      login_user(user)
      return redirect(url_for('secrets'))
  else:
    return render_template("login.html", login=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
  return render_template("secrets.html", name=current_user.name, login=True)


@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
  return send_from_directory(directory='static/files', filename='cheat_sheet.pdf')


if __name__ == "__main__":
  app.run(debug=True)
