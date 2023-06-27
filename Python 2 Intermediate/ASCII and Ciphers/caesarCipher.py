# main.py
#Defining varibles
eM = input("Type in your message to encrypt: ")
eK = input("Type in the key you wish to use: ")
eML = len(eM)
nEM = ""
#Defining dEM to print
for i in range(0, eML, 1):
  if ord(eM[i]) + int(eK) > 122:
     left = (ord(eM[i]) + int(eK)) % 122
     addLeft = 96 + left
     nEM += str(chr(addLeft))
  elif ord(eM[i]) + int(eK) < 122:
    nEM += str(chr(ord(eM[i]) + int(eK)))
#Print nEM
print(nEM)
#Defining varibles
dM = input("Type in your message to decrypt: ")
dK = input("Type in the decryption key: ")
dML = len(dM)
dEM = ""
#Defining dEM to print
for i in range(0, dML, 1):
  if ord(dM[i]) - int(dK) == 32:
    dEM += " "
  elif ord(dM[i]) - int(dK) < 97:
       left = (ord(dM[i]) - int(dK))
       wLeft = 97 - left 
       addLeft = 123 - wLeft
       dEM += str(chr(addLeft))
  elif ord(dM[i]) - int(dK) > 96:
    dEM += str(chr(ord(dM[i]) - int(dK)))
#Print dEM
print(dEM)