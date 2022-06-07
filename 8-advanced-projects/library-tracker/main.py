from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create table
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  author = db.Column(db.String(250), nullable=False)
  rating = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return f'<Book {self.title}>'
db.create_all()


@app.route('/')
def home():
  all_books = db.session.query(Book).all()
  return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
  if request.method == 'POST':
    new = {
      'title': request.form['title'],
      'author': request.form['author'],
      'rating': request.form['rating']
    }
    new = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
    db.session.add(new)
    db.session.commit()
    return redirect(url_for('home'))
  else:
    return render_template('add.html')


@app.route('/edit', methods=["GET", "POST"])
def edit():
  if request.method == 'POST':
    book = Book.query.get(request.form['id'])
    book.rating = request.form['rating']
    db.session.commit()
    return redirect(url_for('home'))
  else:
    book = Book.query.get(request.args.get('id'))
    return render_template('edit.html', book=book)


@app.route('/delete')
def delete():
  book = Book.query.get(request.args.get('id'))
  db.session.delete(book)
  db.session.commit()
  return redirect(url_for('home'))

if __name__ == "__main__":
  app.run(debug=True)

