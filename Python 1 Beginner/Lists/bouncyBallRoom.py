import turtle
import random

Tim = turtle.Turtle()
Tim.speed(100)

def drawSquare():
  Tim.penup()
  Tim.goto(-250, 250)
  Tim.pendown()
  for i in range(4):
    Tim.forward(500)
    Tim.right(90)

def createTurtle(tNumber):
  tNumber.shape('circle')
  tNumber.color(255, 0, 0)
  x = random.randint(-235, 235)
  y = random.randint(-235, 235)
  tRight = random.randint(0, 359)
  tNumber.penup()
  tNumber.goto(x, y)
  tNumber.right(tRight)
  tNumber.speed(100)
  
drawSquare()

T1 = turtle.Turtle()
createTurtle(T1)
T2 = turtle.Turtle()
createTurtle(T2)
T3 = turtle.Turtle()
createTurtle(T3)
T4 = turtle.Turtle()
createTurtle(T4)
T5 = turtle.Turtle()
createTurtle(T5)
T6 = turtle.Turtle()
createTurtle(T6)
T7 = turtle.Turtle()
createTurtle(T7)
T8 = turtle.Turtle()
createTurtle(T8)
T9 = turtle.Turtle()
createTurtle(T9)
T10 = turtle.Turtle()
createTurtle(T10)

listOfTurtles = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]

while True:
  for turtle in listOfTurtles:
    if turtle.xcor() < 238 and turtle.xcor() > -238 and turtle.ycor() < 238 and turtle.ycor() < -238:
      turtle.forward(5)
    else:
      turtle.right(180)
      turtle.forward(5)