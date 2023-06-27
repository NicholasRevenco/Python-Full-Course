# main.py
player1 = input("Player 1, please pick rock, paper, or scissors: ").lower()
player2 = input("Player 2, please pick rock, paper, or scissors: ").lower()

if player1 != "rock" and player1 != "paper" and player1 != "scissors":
  print("Player 1 did not pick rock, paper, or scissors.")
if player2 != "rock" and player2 != "paper" and player2 != "scissors":
  print("Player 2 did not pick rock, paper, or scissors.")

if player1 ==  player2:
  print("Tie!")
elif player1 == "rock":
  if player2 == "scissors":
    print("Player 1 wins!")
  elif player2 == "paper":
    print("Player 2 wins!")
elif player1 == "scissors":
  if player2 == "paper":
    print("Player 1 wins!")
  elif player2 == "rock":
    print("Player 2 wins!")
elif player1 == "paper":
  if player2 == "rock":
    print("Player 1 wins!")
  elif player2 == "scissors":
    print("Player 2 wins!")