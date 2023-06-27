import turtle
import random

Tim = turtle.Turtle()

Tim.speed(100)
Tim.right(90)


def drawLines():
  xLine = 0
  number = 1
  
  for i in range(15):
    xLine = i*20-150
    Tim.penup()
    Tim.goto(xLine, 100)
    Tim.pendown()
    Tim.write(number)
    Tim.forward(100)
    number += 1

def makeTurtleCharacteristics(T, rcolor, gcolor, bcolor, xcordinate, ycordinate):
  T.shape('turtle')
  T.color(rcolor, gcolor, bcolor)
  T.penup()
  T.goto(xcordinate, ycordinate)
  T.pendown()
  
def createTurtles():
  T1 = turtle.Turtle()
  makeTurtleCharacteristics(T1, 255, 0, 0, -150, 75)
  T2 = turtle.Turtle()
  makeTurtleCharacteristics(T2, 0, 255, 0, -150, 50)
  T3 = turtle.Turtle()
  makeTurtleCharacteristics(T3, 0, 0, 255, -150, 25)
  return T1, T2, T3

def Race():
  T1X = 0
  T1Total = 0
  T2X = 0
  T2Total = 0
  T3X = 0
  T3Total = 0
  for i in range(100):
    T1X = random.randint(0, 7)
    T1.forward(T1X)
    T1Total += T1X
    T2X = random.randint(0, 7)
    T2.forward(T2X)
    T2Total += T2X
    T3X = random.randint(0, 7)
    T3.forward(T3X)
    T3Total += T3X
  return T1Total, T2Total, T3Total

def winnings():
  if T1Total > T2Total and T1Total > T3Total:
    T1.write('I win!', font=("Arial", 15, "normal"))
  elif T2Total > T1Total and T2Total > T3Total:
    T2.write("I win!", font=("Arial", 15, "normal"))
  elif T3Total > T1Total and T3Total > T2Total:
    T3.write("I win!", font=("Arial", 15, "normal"))
  elif T1Total == T2Total and T2Total == T3Total:
    T1Actual.write('Tie!')
    T2Actual.write('Tie!')
    T3Actual.write('Tie!')
  elif T1Total == T2Total:
    T1.write('Tie!')
    T2.write('Tie!')
  elif T1Total == T3Total:
    T1.write('Tie!')
    T3.write('Tie!')
  else:
    T2.write('Tie!')
    T3.write('Tie!')  
  
drawLines()

T1, T2, T3 = createTurtles()

T1Total, T2Total, T3Total = Race()

winnings()