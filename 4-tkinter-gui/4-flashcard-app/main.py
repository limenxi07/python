BACKGROUND_COLOUR = "#B1DDC6"
from tkinter import *
import pandas, random

newc = {}
try:
  dataf = pandas.read_csv("4-tkinter-gui/4-flashcard-app/words_to_learn.csv")
except FileNotFoundError:
  dataf = pandas.read_csv("4-tkinter-gui/4-flashcard-app/french_words.csv")
finally:
  data = dataf.to_dict(orient="records")


## GENERATE NEW CARD
def wrong():
  global newc, timer
  newc = random.choice(data)
  window.after_cancel(timer)
  canvas.itemconfig(cardbg, image=card_front)
  canvas.itemconfig(title, text="French", fill="black")
  canvas.itemconfig(word, text=newc["French"], fill="black")
  timer = window.after(3000, func=flip)

def flip():
  canvas.itemconfig(cardbg, image=card_back)
  canvas.itemconfig(title, fill="#fff", text="English")
  canvas.itemconfig(word, fill="#fff", text=newc["English"])


## GRADING CARDS
def correct():
  data.remove(newc)
  pandas.DataFrame(data).to_csv("4-tkinter-gui/4-flashcard-app/words_to_learn.csv", index=False)
  wrong()


## UI SETUP
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOUR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_back = PhotoImage(file="4-tkinter-gui/4-flashcard-app/card_back.png")
card_front = PhotoImage(file="4-tkinter-gui/4-flashcard-app/card_front.png")
cardbg = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOUR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_icon = PhotoImage(file="4-tkinter-gui/4-flashcard-app/right.png")
wrong_icon = PhotoImage(file="4-tkinter-gui/4-flashcard-app/wrong.png")
rightb = Button(image=right_icon, highlightthickness=0, command=correct)
wrongb = Button(image=wrong_icon, highlightthickness=0, command=wrong)
rightb.grid(column=1, row=1)
wrongb.grid(column=0, row=1)

timer = window.after(3000, func=flip)
wrong()


window.mainloop()