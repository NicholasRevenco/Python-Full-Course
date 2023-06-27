import random
import time

#Pick 7 random letters in the alphabet from a list
#Ask the user for a word, and check if all of the letters in the word equal to one of the letters in the 7 random letters
#If the word is vaild, add the length of that word to the total anount of points the user has
#If the word is not valid, print that the word is invalid
#If a time of 60 seconds has gone since the start of the game, end the game, and print out the amount of points the user has

# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = [x.strip() for x in validWords]
f.close()
#The lists, sets, and variables that will not be reseted (being different from the variables added in the while loop)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
all_words = set()
given_letters = set()
score = 0
#The while loop that determines the 7 letters that the user would use
while True:
  random_letter = random.randint(0, 25)
  if len(given_letters) < 7:
    given_letters.add(alphabet[random_letter])
  else:
    break
#The first messages that ask the user to press "enter" to start the game
begin = input("Welcome to Wordsmith! In this game, come up with as many words as you can using the seven letters you are given. Press enter to begin!")
print("Ready....")
time.sleep(1)
print("Set....")
time.sleep(1)
print("Go!\n\nYour random letters are:\n" + str(given_letters))
past_time = time.time()
#The while loop that controls the game
while True:
  #The variables that reset each time the while loop loops around
  user_word = input("\nEnter a word: ")
  check = ""
  number = 0
  letter_usage = 0
  letter_check = len(user_word)*6
  #Checks if all of the letters that the user gave is one of the 7 given letters
  for letter in user_word:
    for letter2 in given_letters:
      if letter == letter2:
        check += letter
      else:
        letter_usage += 1
  #Checks if the word given by the user has allready been given before
  for words in all_words:
    if check == words:
      print("You have already entered this word! Your score is: " + str(score))
      number += 1
  #If the user inputs a word that has a letter that is not one of the 7 words
  if letter_usage != letter_check:
    print("You can only use the 7 letters you were given!")
    number += 1
  #Checks if the word is valid of the 37000 words
  if number == 0:
    if check in validWords:
      score += len(check)
      print("Valid word! Your score is: " + str(score))
      all_words.add(check)
    else:
      print("Word is not valid. Please try again.")
  #If, since the start of the game, 60 seconds has passed, the game will end
  if time.time() - past_time > 60:
    print("Game over!\nFinal score: " + str(score))
    break