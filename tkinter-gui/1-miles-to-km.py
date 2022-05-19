from tkinter import *
font = ("Arial", 16)

window = Tk()
window.title("Miles to km converter")
window.minsize(width=800, height=400)
window.config(padx=300, pady=180)

miles = Label(text="Miles", font=font)
equal = Label(text="is equal to", font=font)
km = Label(text="Km", font=font)
result = Label(text="0", font=font)

user = Entry(width=10)
user.insert(END, string="0")
def button_clicked():
  m = float(user.get())
  result["text"] = str(round(m * 1.60934, 2))
button = Button(text="Calculate", command=button_clicked, font=font)

equal.grid(column=0, row=1)
user.grid(column=1, row=0)
miles.grid(column=2, row=0)
result.grid(column=1, row=1)
km.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()