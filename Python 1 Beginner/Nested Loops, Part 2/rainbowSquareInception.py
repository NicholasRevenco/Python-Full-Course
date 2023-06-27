import turtle

Tim = turtle.Turtle()

Tim.speed(1000)
tlength = 10
Tim.left(10)

r = 0
g = 0
b = 0

for i in range(36):
  Tim.color(r, g, b)
  Tim.right(10)
  for i in range(15):
    for i in range(4):
      Tim.forward(tlength)
      Tim.right(90)
    tlength += 10
  tlength = 10
  b += 10