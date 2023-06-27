# main.py
import random
import time

#Pseudocode:
#Print information of instructions
#Two random numbers between two and eleven will be the player's hand in a list
#If the player's hand is already 21, the player wins by default
#Ask the user to either hit or stay based on their hand
#If the user asks to hit, add a random number between two and eleven to the player's hand
#If the player's hand is above 21 after hitting, print the player has busted
#If the player's hand is below 21, ask the user to either hit or stay again
#If the player's hand is 21, the player wins by default
#If the player asks to stay, generate two random numbers between two and eleven, of which will be the computer's hand against the player
#If the computer's hand is below seventeen, the computer will generate another number for itself to add to its hand
#If the computer's hand is above 21 after hitting, the player wins
#If the computer's hand is 21, the computer wins by default
#If the player's hands are both the same, the game is a tie
#Based on the two player's hands, whoever gets closer to 21 wins
#Ask the user to press "enter" to play again

#Print information of instructions
print("Welcome to the game of Blackjack! In this game, you will be dealt two cards to start. Your goal is to get as close to 21 as possible without going over - or busting! In this simple version of Blackjack, we only use 2 through 11(Ace).\nThe dealer will first ask you to hit (take another card) or stay. As long as you don't bust, once you decide to stay, the dealer will then play his hand. The dealer always has to hit until his hand is at least 17. Whoever has the better hand at the end wins!")
start_game = input("\nPress 'Enter' to start playing.")
while True:
  #The variables and lists needed for the game
  player_hand = []
  player_hand_total = 0
  dealer_hand = []
  dealer_hand_total = 0
  player_win = 0
  player_loss = 0
  dealer_lost = 0
  #The cards that the player will be playing with
  for i in range(2):
    random_card = random.randint(2, 11)
    player_hand.append(random_card)
    player_hand_total += random_card
  while player_win == 0:
    #If the player's hand is already 21, the player wins by default
    if player_hand_total == 21:
      print("You have won!\nHere is your hand:\n" + str(player_hand))
      player_win += 1
      break
    #If the player's hand is above 21, the player loses by default
    if player_hand_total == 22:
      print("You have lost!\nHere is your hand:\n" + str(player_hand))
      player_win += 1
      break
    print("\nHere is your hand:\n" + str(player_hand))
    #Ask the user to either hit or stay based on their hand
    player_option = input("Type in H to hit or S to stay: ")
    #If the user asks to hit, add a random number between two and eleven to the player's hand
    if player_option == "H":
      random_card = random.randint(2, 11)
      player_hand.append(random_card)
      player_hand_total += random_card
      #If the player's hand is above 21 after hitting, print the player has busted
      if player_hand_total > 21:
        print("You have busted!\nHere is your hand:\n" + str(player_hand))
        player_win += 1
    #If the player asks to stay, generate two random numbers between two and eleven, of which will be the computer's hand against the player
    else:
      for i in range(2):
        random_card = random.randint(2, 11)
        dealer_hand.append(random_card)
        dealer_hand_total += random_card
      break
  if player_win != 1:
    time.sleep(1)
    if dealer_hand_total == 21:
      print("The dealer has won!")
    print("\nHere is the dealer's hand:\n" + str(dealer_hand))
    #If the computer's hand is below seventeen, the computer will generate another number for itself to add to its hand
    while dealer_hand_total < 17:
      random_card = random.randint(2, 11)
      dealer_hand.append(random_card)
      dealer_hand_total += random_card
      time.sleep(1)
      print("\nThe dealer has chosen to hit.\nHere is the dealer's hand:\n" + str(dealer_hand))
    #When the dealer has a hand above seventeen, the computer will stop hitting
    if dealer_hand_total > 17:
      time.sleep(1)
      print("\nThe dealer has chosen to stay.\nHere is the dealer's hand:\n" + str(dealer_hand))
    #If the computer's hand is above 21 after hitting, the player wins
    time.sleep(1)
    if dealer_hand_total > 21:
      print("\nThe dealer has lost!")
      dealer_lost += 1
    if dealer_lost == 0:
      if dealer_hand_total >= 17:
        #If the computer's hand is 21, the computer wins by default
        if dealer_hand_total == 21:
          print("\nThe dealer has won!")
        #Based on the two player's hands, whoever gets closer to 21 wins
        else:
          if dealer_hand_total > player_hand_total:
            print("\nThe dealer has won!")
          elif player_hand_total > dealer_hand_total:
            print("\nYou have won!")
          #If the player's hands are both the same, the game is a tie
          else:
            print("You and the dealer have the same total of the hand! It is a draw!")
    print("Here is your hand:\n" + str(player_hand) +"\nHere is the dealer's hand:\n" + str(dealer_hand))
  #Ask the user to press "enter" to play again
  play_again = input("\nPress 'Enter' to play again.")