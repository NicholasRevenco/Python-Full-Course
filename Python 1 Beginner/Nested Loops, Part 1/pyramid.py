import turtle

Tim = turtle.Turtle()

tlength = 10
Tim.speed(100)
Tim.right(60)

Tim.penup()
Tim.goto(0,205)
Tim.pendown()

for i in range(50):
  for i in range(3):
    Tim.forward(tlength)
    Tim.right(120)
  tlength = tlength + 10