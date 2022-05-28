from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    
    self.window = Tk()
    self.window.title("Quiz")
    self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
    self.question = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280,)
    self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

    self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
    self.score_text.grid(column=1, row=0)

    self.tick = PhotoImage(file="3-miscellaneous-modules/api-projects/quiz-app/true.png")
    self.cross = PhotoImage(file="3-miscellaneous-modules/api-projects/quiz-app/false.png")
    self.tick_button = Button(image=self.tick, highlightthickness=0, command=self.tick_clicked)
    self.cross_button = Button(image=self.cross, highlightthickness=0, command=self.cross_clicked)
    self.tick_button.grid(column=0, row=2)
    self.cross_button.grid(column=1, row=2)

    self.get_question()

    self.window.mainloop()

  def get_question(self):
    self.canvas.config(bg="white")
    if self.quiz.still_has_questions():
      self.score_text.config(text=f"Score: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question, text=q_text)
    else:
      self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
      self.cross_button.config(state="disabled")
      self.tick_button.config(state="disabled")


  def tick_clicked(self):
    self.give_feedback(self.quiz.check_answer("True"))

  def cross_clicked(self):
    self.give_feedback(self.quiz.check_answer("False"))

  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000, self.get_question)