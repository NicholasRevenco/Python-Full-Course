# main.py
import os
"""f = open("filename.txt", "w+")
f.write("Hello World")
f.close()"""


userInput = input("Input something: ")
file = open("file.txt", "w+")
for i in range(len(userInput)):
  file.write(userInput[i] + "\n")
file.close()

f.readlines()