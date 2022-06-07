from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
all_books = []


@app.route('/')
def home():
  return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
  if request.method == 'POST':
    new = {
      'title': request.form['title'],
      'author': request.form['author'],
      'rating': request.form['rating']
    }
    all_books.append(new)
    return redirect(url_for('home'))
  else:
    return render_template('add.html')


if __name__ == "__main__":
  app.run(debug=True)

