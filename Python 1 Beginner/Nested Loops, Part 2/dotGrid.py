import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)

numRows = random.randint(1, 12)
numCols = random.randint(1, 12)
yaxis = 0

for i in range(numCols):
  for i in range(numRows):
    Tim.dot()
    Tim.penup()
    Tim.forward(25)
    Tim.pendown()
  yaxis -= 25
  Tim.penup()
  Tim.goto(0, yaxis)
  Tim.pendown()