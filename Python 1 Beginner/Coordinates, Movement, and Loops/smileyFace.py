import turtle
Bobby = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('yellow')
Bobby.speed(1000)
Bobby.color('black')
Bobby.penup()
Bobby.goto(-200,200)
Bobby.pendown()
for i in range(2):
  Bobby.forward(25)
  Bobby.right(90)
  Bobby.forward(150)
  Bobby.right(90)
Bobby.penup()
Bobby.goto(50,200)
Bobby.pendown()
for i in range(2):
  Bobby.forward(25)
  Bobby.right(90)
  Bobby.forward(150)
  Bobby.right(90)
Bobby.penup()
Bobby.goto(-200,-50)
Bobby.pendown()
Bobby.right(90)
for i in range(90):
  Bobby.forward(5)
  Bobby.left(2)