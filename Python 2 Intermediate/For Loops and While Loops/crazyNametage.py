# main.py

name = input('What is your name? ')
nameLength = len(name)
changeNameLength = 0

print("Spelling your name...")
for i in range(nameLength):
  print(name[i])

print("Spelling every other letter in your name...")
for i in range(0, nameLength, 2):
  print(name[i])

print("Spelling your name backwards...")  
for i in range(nameLength-1, -1, -1):
  print(name[i])

print("Spelling your name...")
while changeNameLength < nameLength:
  print(name[changeNameLength])
  changeNameLength += 1

changeNameLength = 0
print("Spelling every other letter in your name...")
while changeNameLength < nameLength:
  print(name[changeNameLength])
  changeNameLength += 2

changeNameLength = nameLength
print("Spelling your name backwards...")  
while changeNameLength > 0:
  changeNameLength -= 1
  print(name[changeNameLength])