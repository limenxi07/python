import turtle, pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank-states-img.gif")
turtle.shape("blank-states-img.gif")

data = pandas.read_csv("50-states.csv")
total = data.state.to_list()
guesses = []

while len(guesses) < 50:
  answer = screen.textinput(title=f"{len(guesses)}/50 states correct", prompt="What's the name of another state?").title()
  if answer in total:
    guesses.append(answer)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    pos = data[data.state == answer]
    t.goto(int(pos.x), int(pos.y))
    t.write(answer)
  if answer == "Exit":
    missing = []
    for i in total:
      if i not in guesses:
        missing.append(i)
    pandas.DataFrame(missing).to_csv("states_to_learn.csv")
    break