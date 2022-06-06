import csv
from csv import writer
from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from h11 import Data
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class CafeForm(FlaskForm):
  cafe = StringField('Cafe name', validators=[DataRequired()])
  location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired(), URL()])
  opening = StringField('Opening time', validators=[DataRequired()])
  closing = StringField('Closing time', validators=[DataRequired()])
  coffee = SelectField('Coffee rating', choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'], validators=[DataRequired()])
  wifi = SelectField('WiFi strength rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
  power = SelectField('Power socket availability', choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'], validators=[DataRequired()])
  submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
  return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
  form = CafeForm()
  if form.validate_on_submit():
    data = [form.cafe.data, form.location.data, form.opening.data, form.closing.data, form.coffee.data, form.wifi.data, form.power.data]
    with open('8-advanced-projects/coffee-wifi-project/cafe-data.csv', newline='', mode='a') as file:
      fwriter = writer(file)
      fwriter.writerow(data)
    return redirect(url_for('cafes'))
  return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
  with open('8-advanced-projects/coffee-wifi-project/cafe-data.csv', newline='') as csv_file:
      csv_data = csv.reader(csv_file, delimiter=',')
      list_of_rows = []
      for row in csv_data:
        list_of_rows.append(row)
  return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
  app.run(debug=True)
