import datetime as dt

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  subtitle = db.Column(db.String(250), nullable=False)
  date = db.Column(db.String(250), nullable=False)
  body = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(250), nullable=False)
  img_url = db.Column(db.String(250), nullable=False)
db.create_all()

##WTForm
class CreatePostForm(FlaskForm):
  title = StringField("Blog Post Title", validators=[DataRequired()])
  subtitle = StringField("Subtitle", validators=[DataRequired()])
  author = StringField("Your Name", validators=[DataRequired()])
  img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
  body = CKEditorField("Blog Content", validators=[DataRequired()])
  submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
  posts = BlogPost.query.all()
  return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
  requested_post = None
  posts = BlogPost.query.all()
  for blog_post in posts:
    if blog_post.id == index:
      requested_post = blog_post
  return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/contact")
def contact():
  return render_template("contact.html")


@app.route('/new-post', methods=['GET', 'POST'])
def create():
  form = CreatePostForm()
  if form.validate_on_submit():
    new = BlogPost(
      title=form.title.data,
      subtitle=form.subtitle.data,
      date=dt.datetime.now().strftime('%B %d, %Y'), 
      body=form.body.data,
      author=form.author.data,
      img_url=form.img_url.data
    )
    db.session.add(new)
    db.session.commit()
    return redirect(url_for('home'))
  else:
    return render_template('make-post.html', form=form, heading='New Post')


@app.route('/edit-post/<int:id>', methods=['GET', 'POST'])
def edit(id):
  post = BlogPost.query.get(id)
  form = CreatePostForm(
    title=post.title,
    subtitle=post.subtitle,
    img_url=post.img_url,
    author=post.author,
    body=post.body
  )
  if form.validate_on_submit():
    post.title = form.title.data
    post.subtitle = form.subtitle.data
    post.img_url = form.img_url.data
    post.author = form.author.data
    post.body = form.body.data
    db.session.commit()
    return render_template('post.html', post=post)
  else:
    return render_template('make-post.html', form=form, heading='Edit Post')


@app.route('/delete/<id>')
def delete(id):
  post = BlogPost.query.get(id)
  db.session.delete(post)
  db.session.commit()
  return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
  app.run(debug=True)
