import turtle
Tim = turtle.Turtle()
Tim.speed(100)

def goTo(y):
  Tim.penup()
  Tim.goto(0, y)
  Tim.pendown()

def drawBullsEye():
  bLength = 5
  colorrw = 10
  goToY = 180
  for i in range(5):
    if (colorrw % 2) == 0:
      goTo(goToY)
      Tim.begin_fill()
      Tim.color(255, 0, 0)
      for i in range(180):
        Tim.forward(bLength)
        Tim.right(2)
      Tim.end_fill()
    else:
      goTo(goToY)
      Tim.begin_fill()
      Tim.color(255, 255, 255)
      for i in range(180):
        Tim.forward(bLength)
        Tim.right(2)
      Tim.end_fill()
    goToY -= 30
    bLength -= 1
    colorrw -= 1
  

drawBullsEye()