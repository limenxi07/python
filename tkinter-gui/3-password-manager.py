from tkinter import *
from tkinter import messagebox
import random
import json

# PASSWORD GENERATOR
def generate():
  out = []
  default = [random.randint(8, 10), random.randint(2, 4), random.randint(2, 4)]
  x = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''','0123456789']
  for i in range(3):
    while default[i] > 0:
      out.append(x[i][random.randint(0, len(x[i])-1)])
      default[i] -= 1
  random.shuffle(out)
  passworde.delete(0, END)
  passworde.insert(0, ''.join(out))

# PASSWORD BANK
def add():
  website = websitee.get()
  email = emaile.get()
  password = passworde.get()
  new_data = {
    website: {
      "email": email,
      "password": password,
    }
  }

  if len(website) == 0 or len(password) == 0 or len(email) == 0:
    messagebox.showinfo(title="Error", message="Please don't leave any fields empty.")
  else:
    with open("./data.json", mode="r") as file:
      data = json.load(file)
      data.update(new_data)

    with open("./data.json", mode="w") as file:
      json.dump(data, file, indent=4)

    websitee.delete(0, END)
    passworde.delete(0, END)

# FIND PASSWORD
def password():
  website = websitee.get()
  try:
    with open("./data.json") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No data file found.")
  else:
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# UI SETUP
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=0, row=0, columnspan=3)

websitet = Label(text="Website:")
websitet.grid(column=0, row=1)
emailt = Label(text="Email/Username:")
emailt.grid(column=0, row=2)
passwordt = Label(text="Password:")
passwordt.grid(column=0, row=3)

websitee = Entry(width=21)
websitee.grid(column=1, row=1)
websitee.focus()
emaile = Entry(width=38)
emaile.grid(column=1, row=2, columnspan=2)
emaile.insert(0, "example@example.com")
passworde = Entry(width=21)
passworde.grid(column=1, row=3)

genb = Button(text="Generate password", command=generate)
genb.grid(row=3, column=2)
addb = Button(text="Add", command=add, width=36)
addb.grid(row=4, column=1, columnspan=2)
searchb = Button(text="Search", command=password, width=13)
searchb.grid(row=1, column=2)

window.mainloop()