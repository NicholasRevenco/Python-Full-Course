import turtle 

Tim = turtle.Turtle()
screen = turtle.Screen()

def moveForward():
  Tim.pendown()
  Tim.forward(100)
  
def moveBackward():
  Tim.pendown()
  Tim.backward(100)
  
def turnRight():
  Tim.right(5)
  
def turnLeft():
  Tim.left(5)
  
Tim.goto(0, 0)

screen.onkey(moveForward, "Up")
screen.onkey(moveBackward, "Down")
screen.onkey(turnRight, "Right")
screen.onkey(turnLeft, "Left")

screen.listen()