from turtle import *
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

class Snake:
  start = [(0, 0), (-20, 0), (-40, 0)]
  
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
  
  def create_snake(self):
    for i in self.start:
      self.add_segment(i)
  
  def add_segment(self, pos):
    s = Turtle("square")
    s.color("white")
    s.penup()
    s.goto(pos)
    self.segments.append(s)
  
  def reset(self):
    for i in self.segments:
      i.goto(1000, 1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]
  
  def extend(self):
    self.add_segment(self.segments[-1].position())
  
  def move(self):
    for i in range(len(self.segments) - 1, 0, -1):
      x = self.segments[i - 1].xcor()
      y = self.segments[i - 1].ycor()
      self.segments[i].goto(x, y)
    self.head.forward(20)

  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90)
  
  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)

  def left(self):
    if self.head.heading() != 0:
      self.head.setheading(180)

  def right(self):
    if self.head.heading() != 180:
      self.head.setheading(0)

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("blue")
    self.speed("fastest")
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.refresh()
  
  def refresh(self):
    self.goto(random.randint(-280, 280), random.randint(-280, 280))

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.hs = 0
    self.penup()
    self.hideturtle()
    self.color("white")
    self.goto(0, 270)
    self.update()

  def update(self):
    self.clear()
    self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
  
  def reset(self):
    if self.score > self.hs:
      self.hs = self.score
    self.score = 0
    self.update()

  def nscore(self):
    self.score += 1
    self.update()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.nscore()

  # collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()

  # collision with tail
  for i in snake.segments:
    if i == snake.head:
      pass
    elif snake.head.distance(i) < 10:
      scoreboard.reset()
      snake.reset()

screen.exitonclick()