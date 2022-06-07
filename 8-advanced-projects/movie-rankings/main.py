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


@app.route("/")
def home():
  movies = db.session.query(Movie).all()
  return render_template("index.html", movies=movies)


if __name__ == '__main__':
  app.run(debug=True)
