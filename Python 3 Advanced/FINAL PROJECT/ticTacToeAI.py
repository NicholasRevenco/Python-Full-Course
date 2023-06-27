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

#Homework: found out in the morning that I also had to do the winning move for the computer, but does not work for some reason
'''
elif checkWin(board, win, row, column):
  checkWin(board, win, 'computer')
  board[row][column] = player
  break
elif checkWin(board, win, '1') == True:
  checkWin(board, win, '1')
  board[row][column] = player
  break'''
def secondPlayer(board, player):
  while True:
    if checkWin(board, 'O'):
      board[row][column] = 'O'
      break
    elif checkWin(board, 'X'):
      board[row][column] = 'O'
      break
    if board[1][1] == ' ':
      board[1][1] = player
      break
    else:
      x = random.randint(0, 2)
      y = random.randint(0, 2)
      if board[x][y] == ' ':
        board[x][y] = player
        break
  return board

def checkWin(board, player):
  global row, column
  if board[1][1] == player and board[2][0] == player and board[0][2] == ' ':
    row = 0
    column = 2
    return True
  elif board[0][2] == player and board[1][1] == player and board[2][0] == ' ':
    row = 2
    column = 0
    return True
  elif board[0][0] == player and board[1][1] == player and board[2][2] == ' ':
    row = 2
    column = 2
    return True
  elif board[2][2] == player and board[1][1] == player and board[0][0] == ' ':
    row = 0
    column = 0
    return True
  elif board[1][0] == player and board[1][1] == player and board[1][2] == ' ':
    row = 1
    column = 2
    return True
  elif board[1][1] == player and board[1][2] == player and board[1][0] == ' ':
    row = 1
    column = 0
    return True
  elif board[0][1] == player and board[1][1] == player and board[2][1] == ' ':
    row = 2
    column = 1
    return True
  elif board[1][1] == player and board[2][1] == player and board[0][1] == ' ':
    row = 0
    column = 1
    return True
  elif board[0][0] == player and board[0][1] == player and board[0][2] == ' ':
    row = 0
    column = 2
    return True
  elif board[0][2] == player and board[0][1] == player and board[0][0] == ' ':
    row = 0
    column = 0
    return True
  elif board[0][0] == player and board[1][0] == player and board[2][0] == ' ':
    row = 2
    column = 0
    return True
  elif board[0][2] == player and board[1][2] == player and board[2][2] == ' ':
    row = 2
    column = 2
    return True
  elif board[2][0] == player and board[1][0] == player and board[0][0] == ' ':
    row = 0
    column = 0
    return True
  elif board[2][2] == player and board[1][2] == player and board[0][2] == ' ':
    row = 0
    column = 2
    return True
  elif board[2][0] == player and board[2][1] == player and board[2][2] == ' ':
    row = 2
    column = 2
    return True
  elif board[2][2] == player and board[2][1] == player and board[2][0] == ' ':
    row = 2
    column = 0
    return True
  elif board[0][0] == player and board[0][2] == player and board[0][1] == ' ':
    row = 0
    column = 1
    return True
  elif board[1][0] == player and board[1][2] == player and board[1][1] == ' ':
    row = 1
    column = 1
    return True
  elif board[2][0] == player and board[2][2] == player and board[2][1] == ' ':
    row = 2
    column = 1
    return True
  elif board[0][0] == player and board[2][0] == player and board[1][0] == ' ':
    row = 1
    column = 0
    return True
  elif board[0][1] == player and board[2][1] == player and board[1][1] == ' ':
    row = 1
    column = 1
    return True
  elif board[0][2] == player and board[2][2] == player and board[1][2] == ' ':
    row = 1
    column = 2
    return True
  elif board[0][0] == player and board[2][2] == player and board[1][1] == ' ':
    row = 1
    column = 1
    return True
  elif board[2][0] == player and board[0][2] == player and board[1][1] == ' ':
    row = 1
    column = 1
    return True
  return False

def tie(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == ' ':
        return False
  return True

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