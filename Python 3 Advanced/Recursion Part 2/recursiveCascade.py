# main.py

def staircase_up(string, x):
  if x == len(string):
    return print(string)
  print(string[0:x])
  x += 1
  return staircase_up(string, x)

def staircase_down(string, x):
  if x == 1:
    return print(string[0:1])
  print(string[0:x])
  x -= 1
  return staircase_down(string, x)

staircase_up("upward", 0)
staircase_down("upward", 6)

def up(s):
  if len(s) > 1:
    up(s[:-1])
  print(s)
  
def down(s):
  print(s)
  if len(s) > 1:
    down(s[:-1])
  
up('upward')
down('upward')