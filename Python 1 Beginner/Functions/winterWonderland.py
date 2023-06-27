import turtle
import random

Tim = turtle.Turtle()

Tim.speed(1000)
Tim.pensize(1)

def drawSnowflake(numBranches, branchLength, sideBranchLength):
  xcordinate = random.randint(-350, 350)
  ycordinate = random.randint(-350, 350)
  Tim.penup()
  Tim.goto(xcordinate, ycordinate)
  Tim.pendown()
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  Tim.color(r, g, b)
  for i in range(numBranches):
    Tim.right(360/numBranches)
    Tim.penup()
    Tim.goto(xcordinate, ycordinate)
    Tim.pendown()
    for i in range(10):
      Tim.forward(branchLength)
      Tim.left(60)
      Tim.forward(sideBranchLength)
      Tim.backward(sideBranchLength)
      Tim.right(120)
      Tim.forward(sideBranchLength)
      Tim.backward(sideBranchLength)
      Tim.left(60)


for i in range(10):
  numBranches = random.randint(2, 12)
  branchLength = random.randint(5, 50)
  sideBranchLength = random.randint(5, 25)
  
  drawSnowflake(numBranches, branchLength, sideBranchLength)