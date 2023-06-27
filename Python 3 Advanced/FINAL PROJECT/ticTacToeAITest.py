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

randomWin = 0
AIWin = 0
tieWin = 0

def game(board):
  global randomWin, AIWin, tieWin
  if flip():
    player = 'X'
  else:
    player = 'O'
  winEnd = 0
  while winEnd == 0:
    if player == 'X':
      if win(board, player):
        winEnd = 1
        randomWin += 1
      while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == ' ':
          board[x][y] = player
          player = 'O'
          break
    else:
      board = secondPlayer(board, player)
      if win(board, player):
        winEnd = 1
        AIWin += 1
      player = 'X'
    if tie(board) and winEnd == 0:
      tieWin += 1
      break

for i in range(1000):
  game([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
print("AI player win amount: " + str(AIWin))
print("Random player win amount: " + str(randomWin))
print("Tie of players amount: " + str(tieWin))