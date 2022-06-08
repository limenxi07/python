import os

import requests
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import sqlalchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

API_KEY = os.environ.get('API_KEY')

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


class AddMovieForm(FlaskForm):
  title = StringField('Movie title', validators=[DataRequired()])
  submit = SubmitField('Add movie')


@app.route("/")
def home():
  movies = db.session.query(Movie).order_by(sqlalchemy.sql.expression.desc(Movie.rating))
  return render_template("index.html", movies=movies)


@app.route('/edit', methods=["GET", "POST"])
def edit():
  form = RateMovieForm()
  if request.args.get('id'):
    movie = Movie.query.get(request.args.get('id'))
  else:
    movie = Movie.query.filter_by(title=request.args.get('title')).first()
  if form.validate_on_submit():
    movie.rating = float(form.rating.data)
    movie.review = form.review.data
    db.session.commit()
    return redirect(url_for('home'))
  else:
    return render_template('edit.html', title=movie.title, form=form)


@app.route('/delete')
def delete():
  movie = Movie.query.get(request.args.get('id'))
  db.session.delete(movie)
  db.session.commit()
  return redirect(url_for('home'))


@app.route('/add', methods=["GET", "POST"])
def add():
  form = AddMovieForm()
  if form.validate_on_submit():
    title = form.title.data
    response = requests.get('https://api.themoviedb.org/3/search/movie', params={'api_key': API_KEY, 'query': title})
    titles = response.json()['results']
    return render_template('select.html', titles=titles)
  else:
    return render_template('add.html', form=form)


@app.route('/search')
def search():
  id = int(request.args.get('id'))
  response = requests.get(f'https://api.themoviedb.org/3/movie/{id}', params={'api_key': API_KEY, 'movie_id': id})
  movie = response.json()
  new = Movie(
    title=movie['title'],
    img_url=f"https://image.tmdb.org/t/p/w500{movie['backdrop_path']}",
    year=movie['release_date'].split('-')[0],
    description=movie['overview']
  )
  db.session.add(new)
  db.session.commit()
  return redirect(url_for('edit', title=new.title))


if __name__ == '__main__':
  app.run(debug=True)
