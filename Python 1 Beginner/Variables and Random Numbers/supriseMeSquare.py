import turtle
import random
Tim = turtle.Turtle()
number = random.randint(0, 100)
place = random.randint(-100, 100)
rcolor = random.randint(0, 255)
gcolor = random.randint(0, 255)
bcolor = random.randint(0, 255)
Tim.penup()
Tim.goto(place, place)
Tim.pendown()
Tim.color(rcolor, gcolor, bcolor)
Tim.begin_fill()
for i in range(4):
  Tim.forward(number)
  Tim.right(90)
Tim.end_fill()