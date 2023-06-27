# main.py

def numbers():
  print("")
  global number1, number2
  number1 = input("Input a number: ")
  number2 = input("Input a second number: ")

def sumN():
  numbers()
  print("The sum of " + number1 + " and " + number2 + " is: " + str(int(number1)+int(number2)))
  
def differenceN():
  numbers()
  print("The difference of " + number1 + " and " + number2 + " is: " + str(int(number1)-int(number2)))

def productN():
  numbers()
  number3 = input("Input a third number: ")
  num = int(number1)*int(number2)
  num = num*int(number3)
  print("The product of " + number1 + ",  " + number2 + ", and " + number3 + " is: " + str(num))

def averageN():
  numbers()
  num = int(number1)+int(number2)
  num = num//2
  print("The average of " + number1 + " and " + number2 + " is: " + str(num))

def factorialN():
  print("")
  number1 = input("Input a number: ")
  num = 1
  x = int(number1)
  for i in range(int(number1)):
    num = num*x
    x -= 1
  print("The factorial of " + number1 + " is: " + str(num))

def raisedPoewrN():
  numbers()
  num = pow(int(number1), int(number2))
  print(number1 + " raised to the " + number2 + " power is: " + str(num))

sumN()
differenceN()
productN()
averageN()
factorialN()
raisedPoewrN()