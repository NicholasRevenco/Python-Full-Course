# main.py

"""dict = {"Bob": 24, "Tim":15}
my_list = [1, 2, 3, 4]
print(dict["Bob"])
for key in dict:
  print(key)
  print(dict[key])
  
if "Bob" in dict:
  print('hello')
if "Bobby" in dict:
  print('goodbye')"""


definitionDict = {"hello": "A greeting", "dog": "An animal", "cat": "An animal", "phone": "An electronic", "bird" : "An animal" }
print(definitionDict)

def factorial(n):
  num = 1
  for i in range(1, n+1, 1):
    num = i*num
  return num
  
squareDict = {}
factorialDict = {}
for i in range(1, 25, 1):
  squareDict[i] = i*i
  factorialDict[i] = factorial(i)
print(squareDict)
print(factorialDict)