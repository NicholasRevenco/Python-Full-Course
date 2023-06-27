import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)

def randomSpot():
  x = random.randint(-250, 250)
  y = random.randint(-250, 250)
  Tim.penup()
  Tim.goto(x, y)
  Tim.pendown()

def randomColor():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  Tim.color(r, g, b)

def reset():
  Tim.clear()
  Tim.penup()
  Tim.goto(0, 0)
  Tim.pendown()
  Tim.color(0, 0, 0)
  
def allRandom():
  randomSpot()
  randomColor()

for i in range(2):
  allRandom()

  Tim.forward(100)