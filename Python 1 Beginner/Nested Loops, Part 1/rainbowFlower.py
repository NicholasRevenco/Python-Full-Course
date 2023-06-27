import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)
tlength = 25
tangle = 1

for i in range(6):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  Tim.color(r, g, b)
  Tim.penup()
  Tim.goto(0, 0)
  Tim.pendown()
  for i in range(27):
    Tim.forward(tlength)
    Tim.right(tangle)
    tangle +=5/2
  Tim.right(51)
  tangle = 1