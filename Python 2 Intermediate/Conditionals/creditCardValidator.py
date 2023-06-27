# main.py

cD = input("Enter a credit card number: ")
cDL = len(cD)
sCD = 0

for i in range(0, cDL, 1):
  if i % 2 == 0:
    sCD += int(cD[i]) * 2
  else:
    sCD += int(cD[i])
print("The sum of the digits, with every other digit multiplied by 2 is " + str(sCD) + ".")
if sCD % 10 == 0:
  print("Card valid")
else:
  print("Card invalid")