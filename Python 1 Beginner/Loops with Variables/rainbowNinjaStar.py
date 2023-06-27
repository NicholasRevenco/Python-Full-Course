import turtle

Tim = turtle.Turtle()
Tim.speed(1000)

r = 0
g = 255
b = 0

for i in range(180):
  Tim.color(r, g, b)
  Tim.forward(200)
  Tim.right(45)
  Tim.forward(40)
  Tim.left(90)
  Tim.forward(100)
  Tim.penup()
  Tim.goto(0, 0)
  Tim.pendown()
  Tim.right(47)
  b = b+2.5
  g = g-1.5