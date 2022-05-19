BACKGROUND_COLOUR = "#B1DDC6"
from tkinter import *
import pandas, random

dataf = pandas.read_csv("udemy_workbook/tkinter-gui/4-flashcard-app/french_words.csv")
data = dataf.values.tolist()

## GENERATE NEW CARD
def new():
  newc = random.choice(data)
  print(newc)

## GRADING CARDS
def correct():
  pass

def wrong():
  pass

## UI SETUP
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOUR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_back = PhotoImage(file="udemy_workbook/tkinter-gui/4-flashcard-app/card_back.png")
card_front = PhotoImage(file="udemy_workbook/tkinter-gui/4-flashcard-app/card_back.png")
canvas.create_image(400, 263, image=card_front)     # TO CHANGE!
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="placeholder", font=("Ariel", 60, "bold")) # TO CHANGE!
canvas.grid(column=0, row=0, columnspan=2)

right_icon = PhotoImage(file="udemy_workbook/tkinter-gui/4-flashcard-app/right.png")
wrong_icon = PhotoImage(file="udemy_workbook/tkinter-gui/4-flashcard-app/wrong.png")
rightb = Button(image=right_icon, highlightthickness=0, command=correct)
wrongb = Button(image=wrong_icon, highlightthickness=0, command=wrong)
rightb.grid(column=1, row=1)
wrongb.grid(column=0, row=1)

window.mainloop()

new() 