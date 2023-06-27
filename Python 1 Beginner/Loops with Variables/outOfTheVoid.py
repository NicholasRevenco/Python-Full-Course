import turtle

Tim = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor(0, 0, 0)
Tim.color(255, 255, 255)
Tim.speed(100)

Tim.penup()
Tim.goto(0,250)
Tim.pendown()

tlength = 500
Tim.right(59)

for i in range(422):
  Tim.forward(tlength)
  tlength = tlength - 2.5
  Tim.right(119)