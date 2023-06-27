# main.py
import random
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0
n11 = 0
n12 = 0

def diceRoll():
  num1 = random.randint(1, 6)
  num2 = random.randint(1, 6)
  tNum = num1 + num2
  return tNum

for i in range(1000):
  tNum = diceRoll()
  if tNum == 2:
    n2 += 1
  elif tNum == 3:
    n3 += 1
  elif tNum == 4:
    n4 += 1 
  elif tNum == 5:
    n5 += 1
  elif tNum == 6:
    n6 += 1
  elif tNum == 7:
    n7 += 1 
  elif tNum == 8:
    n8 += 1
  elif tNum == 9:
    n9 += 1
  elif tNum == 10:
    n10 += 1 
  elif tNum == 11:
    n11 += 1
  else:
    n12 += 1

print(str((n2/10)) + "% of your rolls were 2.")
print(str((n3/10)) + "% of your rolls were 3.")
print(str((n4/10)) + "% of your rolls were 4.")
print(str((n5/10)) + "% of your rolls were 5.")
print(str((n6/10)) + "% of your rolls were 6.")
print(str((n7/10)) + "% of your rolls were 7.")
print(str((n8/10)) + "% of your rolls were 8.")
print(str((n9/10)) + "% of your rolls were 9.")
print(str((n10/10)) + "% of your rolls were 10.")
print(str((n11/10)) + "% of your rolls were 11.")
print(str((n12/10)) + "% of your rolls were 12.")
