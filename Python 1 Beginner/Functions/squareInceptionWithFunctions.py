import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)

def drawSquare(sideLength, r, g, b):
  Tim.color(r, g, b)
  for i in range(3):
    for i in range(4):
      Tim.forward(sideLength)
      Tim.right(90)
    sideLength += originalSideLength
  Tim.right(90)

sideLength = random.randint(10, 100)
originalSideLength = sideLength
  
for i in range(4):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  drawSquare(sideLength, r, g, b)