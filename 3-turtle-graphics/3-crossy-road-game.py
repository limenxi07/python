from turtle import *
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Road")
screen.tracer(0)

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("turtle")
    self.goto(0, -280)
    self.setheading(90)
  
  def move(self):
    self.forward(10)

class Car():
  colours = ['264653', '2a9d8f', 'e9c46a', 'f4a261', 'e76f51', '606c38', '283618', 'fefae0', 'dda15e', 'bc6c25', '16697a', '489fb5', '82c0cc', 'ffa62b']

  def __init__(self):
    self.cars = []
    self.speed = 2
  
  def create_car(self):
    if random.randint(1, 17) == 6:
      c = Turtle("square")
      c.shapesize(stretch_wid=1, stretch_len=2)
      c.color('#' + random.choice(self.colours))
      c.penup()
      c.goto(300, random.randint(-250, 250))
      self.cars.append(c)
  
  def move(self):
    for i in self.cars:
      i.backward(self.speed)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.level = 1
    self.penup()
    self.hideturtle()
    self.goto(-280, 250)
    self.update()
  
  def update(self):
    self.clear()
    self.write(f"Level: {self.level}", font=("Courier", 24, "normal"))
  
  def nlevel(self):
    self.level += 1
    self.update()

player = Player()
car = Car()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

cont = True
while cont:
  screen.update()
  car.create_car()
  car.move()

  # collision with top (level up)
  if player.ycor() > 280:
    scoreboard.nlevel()
    car.speed += 2
    player.goto(0, -280)

  # collision with car
  for i in car.cars:
    if i.distance(player) < 20:
      cont = False
      scoreboard.goto(0, 0)
      scoreboard.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()