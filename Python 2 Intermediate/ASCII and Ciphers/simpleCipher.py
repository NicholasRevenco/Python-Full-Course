# main.py
#Defining varibles
message = input('Type in your message to encrypt: ')
messageLenth = len(message)
messageString = ""
#A for loop that adds the numbers to messageString
for i in range(0, messageLenth, 1):
  messageString += str(ord(message[i]))
  messageString += " "
#Print the numbers resulting of the ASCII convertion
print(messageString)
#Defining varibles
enM = input('Type in your message to encrypt: ')
enK = input('Type the key you wish to use: ')
enML = len(message)
enMS = ""
#A for loop that adds the numbers to enMS, with the key number
for i in range(0, enML, 1):
  enMS += str(ord(enM[i])+int(enK))
  enMS += " "
#Print the numbers resulting of the ASCII convertion
print(enMS)
