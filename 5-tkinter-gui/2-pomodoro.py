from tkinter import *
import math
reps = 0
timer = None

# TIMER MECHANISM
def start():
  global reps
  reps += 1

  if reps % 8 == 0:
    countdown(20 * 60)
    text.config(text="Long break", fg="#e7305b")
  elif reps % 2 == 0:
    countdown(5 * 60)
    text.config(text="Break", fg="#e2979c")
  else:
    countdown(25 * 60)
    text.config(text="Work", fg="#9bdeac")

# RESET MECHANISM
def reset():
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(clock, text="00:00")
  text.config(text="Timer")
  checks.config(text="")
  reps = 0

# COUNTDOWN MECHANISM
def countdown(x):
  m = math.floor(x/60)
  s = x % 60
  if s < 10:
    s = f"0{s}"
  
  canvas.itemconfig(clock, text=f"{m}:{s}")
  if x > 0:
    global timer
    timer = window.after(1000, countdown, x - 1)
  else:
    start()
    total = ""
    for _ in range(math.floor(reps/2)):
      total += "✔"
    checks.config(text=total)

# UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#f7f5dd")

text = Label(text="Timer", bg="#f7f5dd", fg="#9bdeac", font=("Calibri", 35, "bold"))
text.grid(column=1, row=0)
startb = Button(text="Start", highlightthickness=0, command=start)
startb.grid(column=0, row=2)
resetb = Button(text="Reset", highlightthickness=0, command=reset)
resetb.grid(column=2, row=2)
checks = Label(fg="#9bdeac", bg="#f7f5dd")
checks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg="#f7f5dd", highlightthickness=0) # allows layers of widgets, highlightthickness removes white border around image
photo = PhotoImage(file="./tomato.png") # to get image from file
canvas.create_image(100, 112, image=photo) # provide coordinates
clock = canvas.create_text(103, 130, text="00:00", fill="white", font=("Courier", 35, "bold")) # provide coordinates
canvas.grid(column=1, row=1)

window.mainloop()