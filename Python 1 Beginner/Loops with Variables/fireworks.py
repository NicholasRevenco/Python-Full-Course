import turtle
import random

Tim = turtle.Turtle()
Tim.speed(100)
lineLength = 1
for i in range(200):
  rcolor = random.randint(0, 255)
  gcolor = random.randint(0, 255)
  bcolor = random.randint(0, 255)
  Tim.color(rcolor, gcolor, bcolor)
  x = i
  Tim.forward(15+x)
  Tim.forward(-15-x)
  Tim.right(5)