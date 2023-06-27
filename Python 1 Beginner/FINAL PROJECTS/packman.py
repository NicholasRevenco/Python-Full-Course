import turtle
import random

turnUp = 0
turnDown = 0
turnRight = 0
turnLeft = 0
lifeTB = 0
lifesLeft = 0
scoreKeeper = 0

def penUpGo(x, y):
  drawT.penup()
  drawT.goto(x, y)
  drawT.pendown()

def penUpForward(f):
  drawT.penup()
  drawT.forward(f)
  drawT.pendown()

def playerUp():
  global turnUp
  turnUp += 1

def playerDown():
  global turnDown
  turnDown += 1

def playerRight():
  global turnRight
  turnRight += 1

def playerLeft():
  global turnLeft
  turnLeft += 1

def distanceGo():
  player.goto(0, -105)
  player.setheading(0)
  enemy1.goto(0, 15)
  enemy1.setheading(90)
  enemy2.goto(0, 15)
  enemy2.setheading(90)
  enemy3.goto(0, 15)
  enemy3.setheading(90)
  
def makeEnemy(enemyT, color):
  enemyT.speed(100)
  enemyT.penup()
  enemyT.goto(0, 15)
  enemyT.left(90)
  enemyT.color(color)

def createLife(lifeT, x, y):
  lifeT.speed(100)
  screen.register_shape("packman", ((0, -3), (6, 6), (7.5, 4.5), (8, 3), (8.5, 1.5), (9, 0), (8.5, -1.5), (8, -3), (7.5, -4.5), (6, -6), (4.5, -7.5), (0, -9), (-4.5, -7.5), (-6, -6), (-7.5, -4.5), (-8, -3), (-8.5, -1.5), (-9, 0), (-8.5, 1.5), (-8, 3), (-7.5, 4.5), (-6, 6)))
  lifeT.shape("packman")
  lifeT.color('yellow')
  lifeT.penup()
  lifeT.goto(x, y)
  lifeT.right(180)

def scoreTM(scoreT, x, y):
  scoreT.speed(100)
  scoreT.penup()
  scoreT.goto(x, y)
  scoreT.color('yellow')
  screen.register_shape("square", ((-4, -4), (-4, 4), (4, 4), (4, -4)))
  scoreT.shape('square')

screen = turtle.Screen()
screen.bgcolor('black')
screen.tracer(0)

screen.onkey(playerUp, "Up")
screen.onkey(playerDown, "Down")
screen.onkey(playerRight, "Right")
screen.onkey(playerLeft, "Left")
screen.listen()

player = turtle.Turtle()
player.speed(100)
player.penup()
player.goto(0, -105)
screen.register_shape("packman", ((0, -3), (6, 6), (7.5, 4.5), (8, 3), (8.5, 1.5), (9, 0), (8.5, -1.5), (8, -3), (7.5, -4.5), (6, -6), (4.5, -7.5), (0, -9), (-4.5, -7.5), (-6, -6), (-7.5, -4.5), (-8, -3), (-8.5, -1.5), (-9, 0), (-8.5, 1.5), (-8, 3), (-7.5, 4.5), (-6, 6)))
player.shape("packman")
player.color('yellow')

score1 = turtle.Turtle()
scoreTM(score1, -185, 185)
score2 = turtle.Turtle()
scoreTM(score2, -155, 185)
score3 = turtle.Turtle()
scoreTM(score3, -125, 185)
score4 = turtle.Turtle()
scoreTM(score4, -95, 185)
score5 = turtle.Turtle()
scoreTM(score5, -65, 185)
score6 = turtle.Turtle()
scoreTM(score6, -35, 185)
score7 = turtle.Turtle()
scoreTM(score7, 0, 185)
score8 = turtle.Turtle()
scoreTM(score8, 35, 185)
score9 = turtle.Turtle()
scoreTM(score9, 65, 185)
score10 = turtle.Turtle()
scoreTM(score10, 95, 185)
score11 = turtle.Turtle()
scoreTM(score11, 125, 185)
score12 = turtle.Turtle()
scoreTM(score12, 155, 185)
score13 = turtle.Turtle()
scoreTM(score13, 185, 185)
score14 = turtle.Turtle()
scoreTM(score14, 0, 155)
score15 = turtle.Turtle()
scoreTM(score15, -185, -185)
score16 = turtle.Turtle()
scoreTM(score16, -155, -185)
score17 = turtle.Turtle()
scoreTM(score17, -125, -185)
score18 = turtle.Turtle()
scoreTM(score18, -95, -185)
score19 = turtle.Turtle()
scoreTM(score19, -65, -185)
score20 = turtle.Turtle()
scoreTM(score20, -35, -185)
score21 = turtle.Turtle()
scoreTM(score21, 0, -185)
score22 = turtle.Turtle()
scoreTM(score22, 35, -185)
score23 = turtle.Turtle()
scoreTM(score23, 65, -185)
score24 = turtle.Turtle()
scoreTM(score24, 95, -185)
score25 = turtle.Turtle()
scoreTM(score25, 125, -185)
score26 = turtle.Turtle()
scoreTM(score26, 155, -185)
score27 = turtle.Turtle()
scoreTM(score27, 185, -185)
score28 = turtle.Turtle()
scoreTM(score28, 0, -155)
score29 = turtle.Turtle()
scoreTM(score29, -185, -155)
score30 = turtle.Turtle()
scoreTM(score30, -185, -125)
score31 = turtle.Turtle()
scoreTM(score31, -185, -95)
score32 = turtle.Turtle()
scoreTM(score32, -185, -65)
score33 = turtle.Turtle()
scoreTM(score33, -185, -35)
score34 = turtle.Turtle()
scoreTM(score34, -185, 0)
score35 = turtle.Turtle()
scoreTM(score35, -185, 35)
score36 = turtle.Turtle()
scoreTM(score36, -185, 65)
score37 = turtle.Turtle()
scoreTM(score37, -185, 95)
score38 = turtle.Turtle()
scoreTM(score38, -185, 125)
score39 = turtle.Turtle()
scoreTM(score39, -185, 155)
score41 = turtle.Turtle()
scoreTM(score41, 185, -155)
score42 = turtle.Turtle()
scoreTM(score42, 185, -125)
score43 = turtle.Turtle()
scoreTM(score43, 185, -95)
score44 = turtle.Turtle()
scoreTM(score44, 185, -65)
score45 = turtle.Turtle()
scoreTM(score45, 185, -35)
score46 = turtle.Turtle()
scoreTM(score46, 185, 0)
score47 = turtle.Turtle()
scoreTM(score47, 185, 35)
score48 = turtle.Turtle()
scoreTM(score48, 185, 65)
score49 = turtle.Turtle()
scoreTM(score49, 185, 95)
score50 = turtle.Turtle()
scoreTM(score50, 185, 125)
score51 = turtle.Turtle()
scoreTM(score51, 185, 155)
score53 = turtle.Turtle()
scoreTM(score53, 0, 135)
score54 = turtle.Turtle()
scoreTM(score54, 0, -135)
score55 = turtle.Turtle()
scoreTM(score55, -155, 0)
score56 = turtle.Turtle()
scoreTM(score56, -135, 0)
score57 = turtle.Turtle()
scoreTM(score57, 155, 0)
score58 = turtle.Turtle()
scoreTM(score58, 135, 0)
score59 = turtle.Turtle()
scoreTM(score59, -105, 0)
score60 = turtle.Turtle()
scoreTM(score60, -105, -25)
score61 = turtle.Turtle()
scoreTM(score61, -105, -52.5)
score62 = turtle.Turtle()
scoreTM(score62, -105, -80)
score63 = turtle.Turtle()
scoreTM(score63, -105, -105)
score64 = turtle.Turtle()
scoreTM(score64, 105, 0)
score65 = turtle.Turtle()
scoreTM(score65, 105, -25)
score66 = turtle.Turtle()
scoreTM(score66, 105, -52.5)
score67 = turtle.Turtle()
scoreTM(score67, 105, -80)
score68 = turtle.Turtle()
scoreTM(score68, 105, -105)
score69 = turtle.Turtle()
scoreTM(score69, -80, -105)
score70 = turtle.Turtle()
scoreTM(score70, -50, -105)
score71 = turtle.Turtle()
scoreTM(score71, -20, -105)
score72 = turtle.Turtle()
scoreTM(score72, 20, -105)
score73 = turtle.Turtle()
scoreTM(score73, 50, -105)
score74 = turtle.Turtle()
scoreTM(score74, 80, -105)

scoreDots = [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, score11, score12, score13, score14, score15, score16, score17, score18, score19, score20, score21, score22, score23, score24, score25, score26, score27, score28, score29, score30, score31, score32, score33, score34, score35, score36, score37, score38, score39, score41, score42, score43, score44, score45, score46, score47, score48, score49, score50, score51, score53, score54, score55, score56, score57, score58, score59, score60, score61, score62, score63, score64, score65, score66, score67, score68, score69, score70, score71, score72, score73, score74]

enemy1 = turtle.Turtle()
makeEnemy(enemy1, 'red')
enemy2 = turtle.Turtle()
makeEnemy(enemy2, 'green')
enemy3 = turtle.Turtle()
makeEnemy(enemy3, 'purple')

enemies = [enemy1, enemy2, enemy3]

life1 = turtle.Turtle()
createLife(life1, -145, -230)
life2 = turtle.Turtle()
createLife(life2, -170, -230)
life3 = turtle.Turtle()
createLife(life3, -195, -230)

scoreWriter = turtle.Turtle()
scoreWriter.speed(100)
screen.register_shape("line", ((0, 0)))
scoreWriter.shape('line')
scoreWriter.penup()
scoreWriter.goto(-195, 230)
scoreWriter.pendown()
scoreWriter.color('white')
scoreWriter.write('Score:', font = ['Arial', 10, 'normal'])

drawT = turtle.Turtle()
drawT.shape('line')
drawT.color(0, 100, 255)
drawT.speed(100)
penUpGo(-200, 200)

for i in range(4):
  drawT.forward(400)
  drawT.right(90)
penUpGo(-170, 170)
for i in range(4):
  drawT.forward(155)
  penUpForward(30)
  drawT.forward(155)
  drawT.right(90)
penUpGo(-15, 170)
drawT.right(90)
drawT.forward(50)
drawT.right(90)
for i in range(4):
  drawT.forward(105)
  drawT.left(90)
  drawT.forward(105)
  drawT.right(90)
  drawT.forward(50)
  drawT.left(90)
  penUpForward(30)
  drawT.left(90)
  drawT.forward(50)
  drawT.right(90)
penUpGo(-15, 90)
for i in range(3):
  drawT.forward(75)
  drawT.left(90)
  drawT.forward(105)
drawT.forward(75)
drawT.left(90)
drawT.forward(75)
penUpGo(-15, 40)
for i in range(2):
  drawT.forward(50)
  drawT.left(90)
drawT.forward(130)
for i in range(2):
  drawT.left(90)
  drawT.forward(50)
drawT.right(90)
drawT.forward(50)
drawT.left(90)
drawT.color(255, 255, 255)
drawT.forward(30)
drawT.color(0, 100, 255)
drawT.left(90)
drawT.forward(50)
penUpGo(-80, -45)
drawT.right(90)
drawT.color('yellow')
drawT.write('PACKMAN', font = ['Arial', 18, 'normal'])
penUpGo(40, -45)
drawT.write('Rushed', font = ['Arial', 8, 'normal'])
penUpGo(-62, -70)
drawT.write('By: Nicholas Revenco', font = ['Arial', 10, 'normal'])

while lifesLeft < 3:
  screen.update()
  player.forward(1)
  '''Boarders:'''
  xcor = player.xcor()
  ycor = player.ycor()
  if player.xcor() < -185:
    player.backward(1)
  elif player.xcor() > 185:
    player.backward(1)
  elif player.ycor() < -185:
    player.backward(1)
  elif player.ycor() > 185:
    player.backward(1)
  elif round(player.xcor()) == 0 and round(player.ycor()) == 104:
    player.backward(1)
  elif round(player.xcor()) == 0 and round(player.ycor()) == -104:
    player.backward(1)
  elif round(player.xcor()) == 104 and round(player.ycor()) == 0:
    player.backward(1)
  elif round(player.xcor()) == -104 and round(player.ycor()) == 0:
    player.backward(1)
  elif round(player.xcor()) == -105 and round(player.ycor()) == 106:
    player.backward(1)
  elif round(player.xcor()) == -106 and round(player.ycor()) == 105:
    player.backward(1)
  elif round(player.xcor()) == 105 and round(player.ycor()) == -106:
    player.backward(1)
  elif round(player.xcor()) == 106 and round(player.ycor()) == -105:
    player.backward(1)
  elif round(player.xcor()) == 105 and round(player.ycor()) == 106:
    player.backward(1)
  elif round(player.xcor()) == 106 and round(player.ycor()) == 105:
    player.backward(1)
  elif round(player.xcor()) == -105 and round(player.ycor()) == -106:
    player.backward(1)
  elif round(player.xcor()) == -106 and round(player.ycor()) == -105:
    player.backward(1)
  '''Horozontal Switches:'''
  if player.xcor() > -115 and player.xcor() < 115 and round(player.ycor()) == -105:
    if turnRight >= 1:
      player.setheading(0)
      turnRight = 0
    elif turnLeft >= 1:
      player.setheading(180)
      turnLeft = 0
  elif player.xcor() > -115 and player.xcor() < 115 and round(player.ycor()) == 105:
    if turnRight >= 1:
      player.setheading(0)
      turnRight = 0
    elif turnLeft >= 1:
      player.setheading(180)
      turnLeft = 0
  elif player.xcor() > -210 and player.xcor() < 210 and round(player.ycor()) == -185:
    if turnRight >= 1:
      player.setheading(0)
      turnRight = 0
    elif turnLeft >= 1:
      player.setheading(180)
      turnLeft = 0
  elif player.xcor() > -210 and player.xcor() < 210 and round(player.ycor()) == 185:
    if turnRight >= 1:
      player.setheading(0)
      turnRight = 0
    elif turnLeft >= 1:
      player.setheading(180)
      turnLeft = 0
  elif player.xcor() > -210 and player.xcor() < 210 and round(player.ycor()) == 0:
    if turnRight >= 1:
      player.setheading(0)
      turnRight = 0
    elif turnLeft >= 1:
      player.setheading(180)
      turnLeft = 0
  '''Verticle Switches:'''
  if round(player.xcor()) == -105 and player.ycor() < 115 and player.ycor() > -115:
    if turnUp >= 1:
      player.setheading(90)
      turnUp = 0
    elif turnDown >= 1:
      player.setheading(270)
      turnDown = 0
  elif round(player.xcor()) == 105 and player.ycor() < 115 and player.ycor() > -115:
    if turnUp >= 1:
      player.setheading(90)
      turnUp = 0
    elif turnDown >= 1:
      player.setheading(270)
      turnDown = 0
  elif round(player.xcor()) == -185 and player.ycor() < 210 and player.ycor() > -210:
    if turnUp >= 1:
      player.setheading(90)
      turnUp = 0
    elif turnDown >= 1:
      player.setheading(270)
      turnDown = 0
  elif round(player.xcor()) == 185 and player.ycor() < 210 and player.ycor() > -210:
    if turnUp >= 1:
      player.setheading(90)
      turnUp = 0
    elif turnDown >= 1:
      player.setheading(270)
      turnDown = 0
  elif round(player.xcor()) == 0 and player.ycor() < 210 and player.ycor() > -210:
    if turnUp >= 1:
      player.setheading(90)
      turnUp = 0
    elif turnDown >= 1:
      player.setheading(270)
      turnDown = 0
  '''Enemy Turns:'''
  for enemy in enemies:
    enemy.forward(1)
    enemyXCor = round(enemy.xcor())
    ememyYCor = round(enemy.ycor())
    if enemyXCor == -105 and ememyYCor == 105:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(0)
      else:
        enemy.setheading(270)
    elif enemyXCor == 105 and ememyYCor == 105:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(180)
      else:
        enemy.setheading(270)
    elif enemyXCor == -105 and ememyYCor == -105:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(0)
      else:
        enemy.setheading(90)
    elif enemyXCor == 105 and ememyYCor == -105:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(90)
      else:
        enemy.setheading(180)
    elif enemyXCor == 105 and ememyYCor == 0:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(0)
      elif num == 1:
        enemy.setheading(90)
      else:
        enemy.setheading(270)
    elif enemyXCor == -105 and ememyYCor == 0:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(180)
      elif num == 1:
        enemy.setheading(90)
      else:
        enemy.setheading(270)
    elif enemyXCor == 0 and ememyYCor == 105:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(90)
      elif num == 1:
        enemy.setheading(0)
      else:
        enemy.setheading(180)
    elif enemyXCor == 0 and ememyYCor == -105:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(270)
      elif num == 1:
        enemy.setheading(0)
      else:
        enemy.setheading(180)
    elif enemyXCor == 185 and ememyYCor == 0:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(180)
      elif num == 1:
        enemy.setheading(90)
      else:
        enemy.setheading(270)
    elif enemyXCor == -185 and ememyYCor == 0:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(270)
      elif num == 1:
        enemy.setheading(0)
      else:
        enemy.setheading(90)
    elif enemyXCor == 0 and ememyYCor == 185:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(0)
      elif num == 1:
        enemy.setheading(180)
      else:
        enemy.setheading(270)
    elif enemyXCor == 0 and ememyYCor == -185:
      num = random.randint(0, 2)
      if num == 0:
        enemy.setheading(0)
      elif num == 1:
        enemy.setheading(180)
      else:
        enemy.setheading(90)
    elif enemyXCor == 185 and ememyYCor == -185:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(90)
      else:
        enemy.setheading(180)
    elif enemyXCor == 185 and ememyYCor == 185:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(180)
      else:
        enemy.setheading(270)
    elif enemyXCor == -185 and ememyYCor == 185:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(0)
      else:
        enemy.setheading(270)
    elif enemyXCor == -185 and ememyYCor == -185:
      num = random.randint(0, 1)
      if num == 0:
        enemy.setheading(90)
      else:
        enemy.setheading(0)
    distanceXEnemy = player.xcor() - enemy.xcor()
    distanceYEnemy = player.ycor() - enemy.ycor()
    if abs(distanceXEnemy) < 5 and abs(distanceYEnemy) < 5:
      distanceGo()
      lifeTB += 1
      if lifeTB == 1:
        life1.color('black')
      elif lifeTB == 2:
        life2.color('black')
      else:
        life3.color('black')
        penUpGo(-35, -240)
        drawT.color('red')
        drawT.write('Game Over!', font = ['Arial', 15, 'normal'])
        lifesLeft = 3
  for scoreDot in scoreDots:
    distanceXDot = player.xcor() - scoreDot.xcor()
    distanceYDot = player.ycor() - scoreDot.ycor()
    if abs(distanceXDot) < 2 and abs(distanceYDot) < 2:
      scoreDot.color('black')
      scoreDot.goto(-250, 250)
      scoreWriter.clear()
      scoreKeeper += 10
      scoreWriter.write('Score:' + str(scoreKeeper), font = ['Arial', 10, 'normal'])
  if scoreKeeper == 700:
    penUpGo(-35, -240)
    drawT.color('green')
    drawT.write('You Win!', font = ['Arial', 15, 'normal'])
    break
screen.update()