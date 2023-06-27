import turtle
import random

Tim = turtle.Turtle()

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
Tim.color(r, g, b)

Tim.speed(100)
Tim.pensize(5)

sbranch = random.randint(5, 12)
sangle = 360/sbranch
Tim.left(sangle)

for i in range(sbranch):
  Tim.penup()
  Tim.goto(0,0)
  Tim.pendown()
  Tim.right(sangle)
  for i in range(10):
    Tim.forward(10)
    Tim.left(60)
    Tim.forward(10)
    Tim.forward(-10)
    Tim.right(120)
    Tim.forward(10)
    Tim.forward(-10)
    Tim.left(60)