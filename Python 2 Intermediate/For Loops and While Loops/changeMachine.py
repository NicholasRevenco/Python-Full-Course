# main.py

aOfM = input("Tell me how many cents you have, and I'll tell you how many quarters are in that amount: ")

aOfMInt = int(aOfM)
numOfQ = 0
numOfD = 0
while aOfMInt > 24:
  aOfMInt -= 25
  numOfQ += 1
print("There are " + str(numOfQ) + " quarters in " + str(aOfM) + " cents.")

print(' ')
aOfM = input("Now, tell me how many cents you have, and I'll tell you how many quarters as well as dimes there are in that amount: ")
aOfMInt = int(aOfM)
numOfQ = 0
while aOfMInt > 24:
  aOfMInt -= 25
  numOfQ += 1
while aOfMInt > 9:
  aOfMInt -= 10
  numOfD += 1
print("There are " + str(numOfQ) + " quarters and " + str(numOfD) + " dimes in " + str(aOfM) + " cents.")

print(' ')
aOfM = input("Finally, tell me how many cents you have, and I'll tell you how many quarters, dimes, nickles, and pennies there are in that amount: ")
aOfMInt = int(aOfM)
numOfQ = 0
numOfD = 0
numOfN = 0
numOfP = 0
while aOfMInt > 24:
  aOfMInt -= 25
  numOfQ += 1
while aOfMInt > 9:
  aOfMInt -= 10
  numOfD += 1
while aOfMInt > 4:
  aOfMInt -= 5
  numOfN += 1
while aOfMInt > 0:
  aOfMInt -= 1
  numOfP += 1
print("There are " + str(numOfQ) + " quarters, " + str(numOfD) + " dimes, " + str(numOfN) + " nickles, and " + str(numOfP) + " pennies in " + str(aOfM) + " cents.")