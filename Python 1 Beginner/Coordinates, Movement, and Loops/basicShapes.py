import turtle
Bobby = turtle.Turtle()
Bobby.speed(100)
Bobby.color('blue')
Bobby.penup()
Bobby.goto(-450, 0)
Bobby.pendown()
for i in range(4):
  Bobby.forward(50)
  Bobby.right(90)
Bobby.penup()
Bobby.goto(-450, 100)
Bobby.pendown()
Bobby.color('red')
for i in range(3):
  Bobby.forward(50)
  Bobby.right(120)
Bobby.penup()
Bobby.goto(-425, 200)
Bobby.pendown()
Bobby.color('green')
for i in range(360):
  Bobby.forward(.5)
  Bobby.right(1)
  
Bobby.penup()
Bobby.goto(-300, 0)
Bobby.pendown()
Bobby.color('black')
for i in range(6):
  Bobby.forward(25)
  Bobby.right(60)
Bobby.penup()
Bobby.goto(-312.5,50)
Bobby.pendown()
Bobby.color('purple')
Bobby.left(90)
for i in range (2):
  Bobby.forward(150)
  Bobby.right(90)
  Bobby.forward(50)
  Bobby.right(90)
Bobby.penup()
Bobby.goto(-200, 100)
Bobby.pendown()
Bobby.color('orange')
for i in range(360):
  Bobby.forward(2.5)
  Bobby.right(1)
Bobby.penup()
Bobby.goto(-145, 175)
Bobby.pendown()
for i in range(360):
  Bobby.forward(.5)
  Bobby.right(1)
Bobby.penup()
Bobby.goto(-25, 175)
Bobby.pendown()
for i in range(360):
  Bobby.forward(.5)
  Bobby.right(1)
Bobby.penup()
Bobby.goto(-75, 110)
Bobby.pendown()
for i in range(10):
  Bobby.forward(10)
  Bobby.right(36)
Bobby.penup()
Bobby.goto(-120, 75)
Bobby.pendown()
Bobby.right(180)
for i in range(180):
  Bobby.forward(1)
  Bobby.left(1)
Bobby.color('red')
Bobby.penup()
Bobby.goto(150, 100)
Bobby.pendown()
for i in range(7):
  Bobby.forward(40)
  Bobby.left(60)
  Bobby.forward(40)
  Bobby.right(120)