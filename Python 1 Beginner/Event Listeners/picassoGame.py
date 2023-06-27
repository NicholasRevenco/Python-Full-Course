import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)

def drawRandom():
  x = random.randint(-250, 250)
  y = random.randint(-250, 250)
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  Tim.penup()
  Tim.goto(x, y)
  Tim.pendown()
  Tim.color(r, g, b)
  rsize = random.randint(1, 100)
  return rsize
  
def drawShape(loopn):
  Tim.pendown()
  rsize = drawRandom()
  Tim.begin_fill()
  for i in range(loopn):
    Tim.forward(rsize)
    Tim.right(360 / loopn)
  Tim.end_fill()
  
def drawSquare():
  drawShape(4)
  
def drawTriangle():
  drawShape(3)

def drawOctogon():
  drawShape(8)
  
def drawPentagon():
  drawShape(5)

screen = turtle.Screen()

Tim.goto(0, 0)

screen.onkey(drawSquare, "Up")
screen.onkey(drawTriangle, "Down")
screen.onkey(drawOctogon, "Right")
screen.onkey(drawPentagon, "Left")

screen.listen()