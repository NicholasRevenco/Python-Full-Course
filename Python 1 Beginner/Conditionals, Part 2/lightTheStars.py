import turtle
import random

Tim = turtle.Turtle()
Tim.shape('turtle')
Tim.color(255, 255, 255)

screen = turtle.Screen()
r = 195
t = 41.5
screen.bgcolor(r, 20, 50)

win = 0
score = 0

def makeDot(dot):
  dot.speed(100)
  x = random.randint(-350, 350)
  y = random.randint(-350, 350)
  dot.shape('circle')
  dot.color(255, 255, 255)
  dot.penup()
  dot.goto(x, y)
  
def goRight():
  Tim.right(10)

def goLeft():
  Tim.left(10)
  
def goForward():
  Tim.forward(10)

def goBackward():
  Tim.backward(10)

def sequence(dot):
  dot.speed(100)
  dot.color(255, 255, 0)
  dot.begin_fill()
  for i in range(5):
    dot.forward(15)
    dot.right(144)
    dot.forward(15)
    dot.left(72)
  dot.end_fill()
  dot.color(r, 20, 50)
  dot.penup()
  dot.goto(-500, -500)

time = turtle.Turtle()
time.speed(100)
time.color(255, 255, 255)
time.penup()
time.goto(-400, 400)
time.pendown()
  
screen.onkey(goRight, 'Right')
screen.onkey(goLeft, 'Left')
screen.onkey(goForward, 'Up')
screen.onkey(goBackward, 'Down')
screen.listen()


dot1 = turtle.Turtle()
makeDot(dot1)
dot2 = turtle.Turtle()
makeDot(dot2)
dot3 = turtle.Turtle()
makeDot(dot3)
dot4 = turtle.Turtle()
makeDot(dot4)
dot5 = turtle.Turtle()
makeDot(dot5)
dot6 = turtle.Turtle()
makeDot(dot6)
dot7 = turtle.Turtle()
makeDot(dot7)
dot8 = turtle.Turtle()
makeDot(dot8)
dot9 = turtle.Turtle()
makeDot(dot9)
dot10 = turtle.Turtle()
makeDot(dot10)

dots = [dot1, dot2, dot3, dot4, dot5, dot6, dot7, dot8, dot9, dot10]

while True:
  for dot in dots:
    xCol = Tim.xcor() - dot.xcor()
    yCol = Tim.ycor() - dot.ycor()
    if abs(xCol) < 25 and abs(yCol) < 25:
      sequence(dot)
      score += 1
  r -= .25
  t -= 0.06125
  time.clear()
  time.write("Time left: " + str(t) + " seconds")
  screen.bgcolor(r, 20, 50)
  if r < 30:
    Tim.write('Game over!')
    break
  if score == 10:
    Tim.write('You win!')
    break