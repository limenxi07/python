import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-ten-movie-rankings.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create table
class Movie(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  year = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String(750), nullable=False)
  rating = db.Column(db.Float, nullable=True)
  ranking = db.Column(db.Integer, nullable=True)
  review = db.Column(db.String(750), nullable=True)
  img_url = db.Column(db.String(250), nullable=False)
db.create_all()


class RateMovieForm(FlaskForm):
  rating = StringField('Your rating (/10)', validators=[DataRequired()])
  review = StringField('Your review', validators=[DataRequired()])
  submit = SubmitField('Submit')


@app.route("/")
def home():
  movies = db.session.query(Movie).all()
  return render_template("index.html", movies=movies)


@app.route('/edit', methods=["GET", "POST"])
def edit():
  form = RateMovieForm()
  movie = Movie.query.get(request.args.get('id'))
  if form.validate_on_submit():
    movie.rating = float(form.rating.data)
    movie.review = form.review.data
    db.session.commit()
    return redirect(url_for('home'))
  else:
    return render_template('edit.html', movie=movie, form=form)

if __name__ == '__main__':
  app.run(debug=True)
