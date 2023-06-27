# main.py
import time
import random

#Pseudocode: Print the first messages to then print out the sentence to type
#From a list, print out a random sentence to print
#Ask the user to type in the sentence, and then press enter to submit
#If the user's sentence is equal to the given sentence, pring out the amount of time it took the user to type out the sentence
#If the user's sentence is not equal to the given sentence, ask the user to re-type the sentence

#Picks one of the message out of the list
sentences = ["If a dog chews shoes, whose shoes does he chose?", "I scream, you scream, we all scream, for ice cream!", "Peter Piper picked a peck of pickled peppers.", "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"]
random_sentence = random.randint(0, 3)
random_sentence = sentences[random_sentence]
#Prints the starting messages after the user inputs "Enter"
enter = input("Welcome to Type Racer. Press Enter to play.")
print("Ready....")
time.sleep(1)
print("Set....")
time.sleep(1)
print("Type!")
print("\n" + random_sentence)
#Finds out if the user's input is equal ot the sentence
time_amount = time.time()
user_input = input("\nType: ")
while user_input != random_sentence:
  print("The sentences do not match! Please try again.")
  user_input = input("\nType: ")
#Once the while loop ends, the computer will print out the amount of time it took to finish the sentence
print("\nYou finished typing in " + str(time.time() - time_amount) + " seconds!")

#7.62939453125e-06