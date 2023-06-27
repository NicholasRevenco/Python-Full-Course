import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)
tlength = 50
Tim.left(90)

for i in range(4):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b  = random.randint(0, 255)
  Tim.color(r, g, b)
  Tim.right(90)
  for i in range(3):
    for i in range(4):
      Tim.forward(tlength)
      Tim.right(90)
    tlength += 25
  tlength = 50