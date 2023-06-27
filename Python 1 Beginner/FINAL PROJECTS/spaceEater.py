import turtle
import random

screen = turtle.Screen()
screen.bgcolor(0, 0, 0)
screen.tracer(0)

def goTo(t, r, g, b, x, y):
  t.speed(100)
  t.color(r, g, b)
  t.penup()
  t.goto(x, y)
  t.pendown()

Tim = turtle.Turtle()
goTo(Tim, 255, 0, 0, -250, 250)

for i in range(4):
  Tim.forward(500)
  Tim.right(90)

scoreT = turtle.Turtle()
goTo(scoreT, 255, 255, 255, -250, 270)

timeT = turtle.Turtle()
goTo(timeT, 255, 255, 255, -250, 290)


player = turtle.Turtle()
player.color(0, 0, 255)
player.shape('turtle')
player.penup()

dots = []
for i in range(10):
  dot = turtle.Turtle()
  dot.shape('circle')
  dot.color(255, 0, 0)
  dots.append(dot)
for dot in dots:
  dot.speed(100)
  dot.penup()
  x = random.randint(-235, 235)
  y = random.randint(-235, 235)
  turnRight = random.randint(0, 359)
  dot.goto(x, y)
  dot.right(turnRight)
  dot.speed(50)

def turnRight():
  player.right(7.5)

def turnLeft():
  player.left(7.5)

screen.onkey(turnRight, "Right")
screen.onkey(turnLeft, "Left")
screen.listen()
screen.update()
score = 0
time = 30

while True:
  screen.update()
  player.forward(3)
  if player.xcor() > 228 or player.xcor() < -228 or player.ycor() > 228 or player.ycor() < -228:
    player.right(180)
  for dot in dots:
    dot.forward(1)
    if dot.xcor() > 238 or dot.xcor() < -238 or dot.ycor() > 238 or dot.ycor() < -238:
      dot.right(180)
    xcor = player.xcor() - dot.xcor()
    ycor = player.ycor() - dot.ycor()
    if abs(xcor) < 15 and abs(ycor) < 15:
      score += 1
      x = random.randint(-235, 235)
      y = random.randint(-235, 235)
      dot.goto(x, y)
  scoreT.clear()
  scoreT.write('Score: ' + str(score))
  time -= 0.02
  timeT.clear()
  timeT.write('Time Remaining: ' + str(round(time, 1)) + ' seconds')
  if time < 0:
    break