import turtle
import random
Tim = turtle.Turtle()
Tim.speed(5)
#Color for bowtie 1
r1color = random.randint(0, 255)
g1color = random.randint(0, 255)
b1color = random.randint(0, 255)
#Color for bowtie 2
r2color = random.randint(0, 255)
g2color = random.randint(0, 255)
b2color = random.randint(0, 255)
#Color for background
r3color = random.randint(0, 255)
g3color = random.randint(0, 255)
b3color = random.randint(0, 255)
#Background sequence
screen = turtle.Screen()
screen.bgcolor(r3color, g3color, b3color)
#Bowtie 1 sequence
Tim.penup()
Tim.goto(0, 0)
Tim.pendown()
Tim.left(30)
Tim.begin_fill()
Tim.color(r1color, g1color, b1color)
for i in range(3):
  Tim.forward(200)
  Tim.right(120)
Tim.end_fill()
#Bowtie 2 sequence
Tim.penup()
Tim.goto(0, 0)
Tim.pendown()
Tim.begin_fill()
Tim.color(r2color, g2color, b2color)
Tim.right(180)
for i in range(3):
  Tim.forward(200)
  Tim.right(120)
Tim.end_fill()