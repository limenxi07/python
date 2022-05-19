from turtle import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

class Paddle(Turtle):
  def __init__(self, pos):
    super().__init__()
    self.penup()
    self.shape("square")
    self.color("white")
    self.turtlesize(stretch_wid=5, stretch_len=1)
    self.goto(pos)
  
  def up(self):
    self.goto((self.xcor(), self.ycor() + 20))
  
  def down(self):
    self.goto((self.xcor(), self.ycor() - 20))

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("white")
    self.speed = 0.1
    self.x = 2
    self.y = 2

  def move(self):
    self.goto((self.xcor() + self.x, self.ycor() + self.y))
  
  def reset(self):
    self.goto(0, 0)
    self.speed = 0.1

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score1 = 0
    self.score2 = 0
    self.penup()
    self.hideturtle()
    self.color("white")
    self.update()
  
  def update(self):
    self.clear()
    self.goto(-100, 200)
    self.write(self.score2, align="center", font=("Courier", 80, "normal"))
    self.goto(100, 200)
    self.write(self.score1, align="center", font=("Courier", 80, "normal"))
  
  def nscore1(self):
    self.score1 += 1
    self.update()
  
  def nscore2(self):
    self.score2 += 1
    self.update()

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

cont = True
while cont:
  screen.update()
  ball.move()

  # collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.y *= -1

  # collision with paddle
  if (ball.distance(paddle1) < 50 and ball.xcor() > 320) or (ball.distance(paddle2) < 50 and ball.xcor() < -320):
    ball.x *= -1

  # miss with paddle 1
  if ball.xcor() > 380:
    scoreboard.nscore2()
    ball.reset()

  # miss with paddle 2
  if ball.xcor() < -380:
    scoreboard.nscore1()
    ball.reset()

screen.exitonclick()