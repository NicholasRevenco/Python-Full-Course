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
  if checkWin(board, 'O'):
    board[row][column] = 'O'
    return board
  elif checkWin(board, 'X'):
    board[row][column] = 'O'
    return board
  for a in range(3):
    for b in range(3):
      if fork(board, 'O', a, b):
        board[a][b] = 'O'
        return board
  for a in range(3):
    for b in range(3):
      if fork(board, 'X', a, b):
        board[a][b] = 'O'
        return board
  if board[1][1] == ' ':
    board[1][1] = player
    return board
  elif board[0][0] == ' ':
    board[0][0] = player
    return board
  elif board[0][2] == ' ':
    board[0][2] = player
    return board
  elif board[2][0] == ' ':
    board[2][0] = player
    return board
  elif board[2][2] == ' ':
    board[2][2] = player
    return board
  elif board[0][1] == ' ':
    board[0][1] = player
    return board
  elif board[1][0] == ' ':
    board[1][0] = player
    return board
  elif board[1][2] == ' ':
    board[1][2] = player
    return board
  elif board[2][1] == ' ':
    board[2][1] = player
    return board
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

def duplicate(board):
  boardDuplicate = [[], [], []]
  for i in range(3):
    for j in range(3):
      boardDuplicate[i].append(board[i][j])
  return boardDuplicate

def fork(board, player, i, j):
  newBoard = duplicate(board)
  good = 0
  if newBoard[i][j] != ' ':
    return False
  newBoard[i][j] = player
  for c in range(3):
    for d in range(3):
      if newBoard[c][d] == ' ':
        newBoard[c][d] = player
      if win(newBoard, player):
        good += 1
        print(good)
        if good >= 2:
          return True
      newBoard[c][d] = ' '
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