import turtle
import random

def shape(TNumber):
  TNumber.shape('turtle')
  TNumber.speed(100)
  TNumber.goto(0, 0)

T1 = turtle.Turtle()
shape(T1)
T2 = turtle.Turtle()
shape(T2)
T3 = turtle.Turtle()
shape(T3)
T4 = turtle.Turtle()
shape(T4)
T5 = turtle.Turtle()
shape(T5)
T6 = turtle.Turtle()
shape(T6)
T7 = turtle.Turtle()
shape(T7)
T8 = turtle.Turtle()
shape(T8)
T9 = turtle.Turtle()
shape(T9)
T10 = turtle.Turtle()
shape(T10)

turtlelist = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10]

for turtle in turtlelist:
 rDegrees = random.randint(0, 360)
 rColor = random.randint(0, 255)
 gColor = random.randint(0, 255)
 bColor = random.randint(0, 255)
 turtle.color(rColor, gColor, bColor)
 turtle.right(rDegrees)
 turtle.forward(200)