# main.py

def exponent(b, p):
  '''if p == 1:
    return b'''
  if p == 0:
    return 1
  return b*exponent(b, p-1)
  
print(exponent(2, 3))