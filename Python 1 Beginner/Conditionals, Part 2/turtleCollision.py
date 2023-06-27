import turtle
import random

player1 = turtle.Turtle()
player2 = turtle.Turtle()
screen = turtle.Screen()

def makePlayer(player, x, y, r, g, b, d):
  player.penup()
  player.goto(x, y)
  player.pendown()
  player.color(r, g, b)
  player.right(d)
  
def player1Right():
  player1.right(10)

def player1Left():
  player1.left(10)

def player2Right():
  player2.right(10)

def player2Left():
  player2.left(10)

def collisionSequence(player):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  player.color(r, g, b)
  player.write("Collision!")

screen.onkey(player1Right, "Right")
screen.onkey(player1Left, "Left")
screen.onkey(player2Right, "A")
screen.onkey(player2Left, "D")
screen.listen()

makePlayer(player1, 100, 0, 255, 0, 0, 180)
makePlayer(player2, -100, 0, 0, 0, 255, 0)

xCor = player1.xcor() - player2.xcor()
yCor = player1.ycor() - player2.ycor()

while True:
  player1.forward(10)
  player2.forward(10)
  xCor = player1.xcor() - player2.xcor()
  yCor = player1.ycor() - player2.ycor()
  if abs(xCor) < 25 and abs(yCor) < 25:
    collisionSequence(player1)
    collisionSequence(player2)

'''while True:
  player1.forward(10)
  player2.forward(10)
  xCor = player1.xcor() - player2.xcor()
  yCor = player1.ycor() - player2.ycor()
  if abs(xCor) > 50 or abs(yCor) > 50:
    print('hello')
  elif abs(xCor) < 50 and abs(yCor) < 50:
    collisionSequence(player1)
    collisionSequence(player2)'''