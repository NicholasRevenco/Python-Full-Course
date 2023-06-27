# main.py
import random

def printBoard(board):
  for i in range(3):
    for j in range(3):
      if j == 2:
        print(" " + board[i][j], end="")
      else:
        print(" " + board[i][j] + " |", end="")
    if i != 2:
      print("\n-––+–––+–––")
  print("\n")
  
def secondPlayer(board, player):
  while True:
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if board[x][y] == ' ':
      board[x][y] = player
      break
  return board


def tie(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        return False
  return True

'''
def tie(board):
  count = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] != ' ':
        count += 1
  if(count == 9):
    return True
  return False
'''

def flip():
  if random.randint(0, 1) == 0:
    return True
  return False

def win(board, player):
  if board[0][0] == player and board[0][1] == player and board[0][2] == player:
    return True
  elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
    return True
  elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
    return True
  elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
    return True
  elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
    return True
  elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
    return True
  elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
    return True
  return False

def game(board):
  if flip():
    player = 'X'
  else:
    player = 'O'
  winEnd = 0
  while winEnd == 0:
    '''
    while True:
      if(player == 'X'):
        if(win(board,player)):
          print("YOU win!")
          break
      else:
        if(win(board,player)):
          print("You lost!")
          break
    '''
    
    printBoard(board)
    if player == 'X':
      while True:
        rowInput = int(input("Pick a row to play: "))
        columnInput = int(input("Pick a column to play: "))
        if rowInput > -1 and columnInput > -1 and rowInput < 3 and columnInput < 3 and board[rowInput][columnInput] == ' ':
          board[rowInput][columnInput] = player
          if win(board, player) == True:
            print("\nYou win!")
            winEnd = 1
          player = 'O'
          break
        else:
          print("Input a valid row or column.")
    else:
      board = secondPlayer(board, player)
      if win(board, player):
        print("\nThe computer wins!")
        winEnd = 1
      player = 'X'
    if tie(board) and winEnd == 0:
      print("\nThe game is a tie!")
      break
  print("\n")
  printBoard(board)

game([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])

#secondPlayer([['O', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'O']], 'X')
#printBoard([['O', 'X', 'X'], ['O', 'X', 'X'], ['O', 'X', 'X']])

#printBoard([['O', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'O']])
#print(win([['O', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'O']], "O"))