# main.py
import time
import random

#Reaction Time game
'''print("This is a simple tool to measure your reaction time.")
while True:
  get_ready = input("\nPress 'A' to begin the game (do not press enter again until you see the 'Click!' message):")
  print(len(get_ready))
  random_time = random.randint(2, 5)
  time.sleep(random_time)
  past_time = time.time()
  click_here = input("Click!")
  if len(click_here) > 1:
    click_here = click_here[0]
  if time.time() - past_time < 0.00015:
    print("\n\nYou pressed 'Enter' before you were able to see the 'Click!' message! Try again.")
    click_here = 0
  else:
    break
print("\nIt took you " + str(time.time() - past_time) + " seconds to react.\n___________________________________________________")'''

while True:
  #Print out the first greeting, game options, and the user's input for one of the game options
  print("Welcome to the Human Benchmark tests.")
  print("\nPress '1' to test your number memory skills.\nPress '2' to test your verbal memory skills.\nPress '3' to test your typing skills.")
  user_game = input("Type here: ")
  not_option = 0
  #The number memory game
  if user_game == '1':
    #Ask the user to press "Enter" to start the game
    enter = input("\nWelcome to Number Memory. Press 'Enter' to play.")
    print("Ready....")
    time.sleep(1)
    print("Set....")
    time.sleep(1)
    print("Remember!")
    level = 1
    while True:
      number = ""
      #Gives the user a number that is based on the level the user is on
      for i in range(level):
        number += str(random.randint(0, 9))
      print("\nNumber: " + number)
      #Gives the user time to remember the word
      time.sleep(level)
      #If the user enters a letter, the game will end
      try:
        user_number = int(input("\n"*50 + "Input the number here: "))
      except:
        print("Only numbers can be entered")
        print("You reached level " + str(level) + ".\n___________________________________________________")
        break
      #Increases the user's level if the user inputs the correct number, or ends the game if the user inputs an incorrect answer
      if user_number == int(number):
        level += 1
      else:
        print("You have reached level " + str(level) + ".\n___________________________________________________")
        break
  elif user_game == '2':
    #Opens the valid_words.txt file with all of the word options
    f = open("valid_words.txt")
    valid_words = f.readlines()
    valid_words = [x.strip() for x in valid_words]
    f.close()
    #The varibales and list needed for the game
    user_life = 3
    score = 0
    first_round = 0
    words_seen = []
    #Ask the user to press "Enter" to start the game
    enter = input("\nWelcome to Verbal Memory. Press 'Enter' to play.")
    print("Ready....")
    time.sleep(1)
    print("Set....")
    time.sleep(1)
    print("Remember!")
    #Actual game runs forever if the user is able to remember all of the words given
    while user_life > 0:
      if first_round != 0:
        #There is a 1/3 chance that the user will be given a word that has been shown before, and a 2/3 chance that a new word will be given
        new_seen = random.randint(0, 2)
        if new_seen == 0:
          random_word = random.choice(words_seen)
        else:
          random_word = random.choice(words_seen)
          random_word = random.choice(valid_words)
          valid_words.remove(random_word)
      #If this round is the first round of the game, give a word from the valid_words.txt
      else:
        random_word = random.choice(valid_words)
        valid_words.remove(random_word)
      #Prints the word and asks the user if the word has been seen before
      print("\nWord: " + random_word)
      user_seen = input("\nPress 'S' if you have seen the word, or press 'N' if the word is new to you: ")
      #Different options for user's input
      if user_seen == 'S' and random_word in words_seen:
        score += 1
      elif user_seen == 'N' and random_word in words_seen:
        user_life -= 1
      elif user_seen == 'N' and random_word not in words_seen:
        score += 1
      elif user_seen == 'S' and random_word not in words_seen:
        user_life -= 1
      else:
        user_life -= 1
      words_seen.append(random_word)
      first_round = +1
      #Prints the user's score and the amount of lives the usr has
      print("\nYour score is: " + str(score) + ".\nYou have " + str(user_life) + " lives left.")
      time.sleep(.5)
    #If the user runs out of lives, the game will end
    print("You have run out of lives. Your final score is: " + str(score) + "\n___________________________________________________")
  #The typing test game
  elif user_game == '3':
      #Picks one of the message out of the list to give to the user
    sentences = ["If a dog chews shoes, whose shoes does he chose?", "I scream, you scream, we all scream, for ice cream!", "Peter Piper picked a peck of pickled peppers.", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"]
    random_sentence = random.randint(0, len(sentences)-1)
    random_sentence = sentences[random_sentence]
    #Ask the user to press "Enter" to start the game
    enter = input("\nWelcome to Type Racer. Press 'Enter' to play.")
    print("Ready....")
    time.sleep(1)
    print("Set....")
    time.sleep(1)
    print("Type!")
    print("\n" + random_sentence)
    #Finds out if the user's input is equal ot the sentence
    time_amount = time.time()
    user_input = input("\nType: ")
    #If the uesr's input does not equal to the sentence, ask the user to type in another answer
    while user_input != random_sentence:
      print("The sentences do not match! Please try again.")
      user_input = input("\nType: ")
    #Print out the amount of time and the speed it took the user to type in the sentence
    print("\nYou finished typing in " + str(time.time() - time_amount) + " seconds!\nYour typing speed was " + str(len(random_sentence)/5/((time.time() - time_amount)/60)) + " words per minute.\n___________________________________________________")
  #If the user picks an option (of a game) that is not one of the three
  else:
    print("That is not an option.\n")
    not_option = 1
  if not_option == 0:
    play_again = input("\nPress 'Enter' to play again!\n___________________________________________________\n")