import turtle

screen = turtle.Screen()

Tim = turtle.Turtle()
Tim.speed(100)

scoreTurtle = turtle.Turtle()
playerTurtle = turtle.Turtle()

def drawSquare():
  Tim.color(255, 0, 0)
  Tim.penup()
  Tim.goto(-250, 250)
  Tim.pendown()
  for i in range(4):
    Tim.forward(500)
    Tim.right(90)

def turnLeft():
  playerTurtle.left(10)
  
def turnRight():
  playerTurtle.right(10)
  
def sTGoTo():
  scoreTurtle.penup()
  scoreTurtle.goto(-250, 260)
  scoreTurtle.pendown()

drawSquare()

screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()

sTGoTo()

goForward = 8
score = 0

while playerTurtle.xcor() < 250 and playerTurtle.xcor() > -250 and playerTurtle.ycor() < 250 and playerTurtle.ycor() > -250:
  playerTurtle.forward(goForward)
  score += goForward
  scoreTurtle.clear()
  scoreTurtle.write("Score:" + str(score))

playerTurtle.write("Out of bounds!")