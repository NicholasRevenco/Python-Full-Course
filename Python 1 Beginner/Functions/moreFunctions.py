import turtle

Tim = turtle.Turtle()

Tim.speed(100)

def drawSquare(sideLength):
  for i in range(4):
    Tim.forward(sideLength)
    Tim.right(90)
  
def drawTriangle(sideLength):
  for i in range(3):
    Tim.forward(sideLength)
    Tim.right(120)

  
sideLength = 200
drawSquare(sideLength)
drawTriangle(sideLength)

sideLength = 20
for i in range(10):
  drawSquare(sideLength)
  sideLength +=5