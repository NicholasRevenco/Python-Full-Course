# main.py
#Lists defined
num = []
wordList = []
perfectSquares = []
removePerfectSquares = []
factorialList = []
userList = [500, 25, 50, 35, 90, 80, 70]
#Variables defined:
factorialNum = 1
totalFactorial = 0
largestNumber = 0
largestNumber = 0
#Print 10 to 0
for i in range(10, 0, -1):
  num.append(i)
print(num)
print("")
#Print word
userWord = input("Type in a word: ")
userWordLength = len(userWord)
for i in range(0, userWordLength, 1):
  wordList.append(userWord[i])
print(wordList)
print("")
#Print perfect squares
for i in range(1, 101, 1):
  perfectSquares.append(i*i)
print(perfectSquares)
print("")
#Remove perfect squares
num = [i for i in perfectSquares if i > 2000 and i < 3000]
for numbers in num:
   if numbers in perfectSquares:
     perfectSquares.remove(numbers)
print(perfectSquares)
print("Here")
#Print factorialLis
for i in range(1, 26, 1):
  factorialNum = i
  track = i-1
  for a in range(i-1):
    factorialNum = factorialNum*track
    track -= 1
  factorialList.append(factorialNum)
  factorialNum = 1
print(factorialList)
print('')
# Print sum of factorials
for i in range(25):
  totalFactorial += factorialList[i]
print(totalFactorial)
print("")
#Print the largest number in a list
for i in range(7):
  if i != 0:
    if userList[i] > userList[i-1] and largestNumber < userList[i]:
      largestNumber = userList[i]
  if largestNumber < userList[0]:
    largestNumber = userList[0]
print(largestNumber)