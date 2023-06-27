import turtle

Tim = turtle.Turtle()

Tim.speed(100)
Tim.right(60)

Tim.penup()
Tim.goto(0, 205)
Tim.pendown()

def drawTriangle(sidelength):
  for i in range(3):
    Tim.forward(sidelength)
    Tim.right(120)

sidelength = 10

for i in range(50):
  drawTriangle(sidelength)
  sidelength += 10