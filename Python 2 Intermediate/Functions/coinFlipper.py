# main.py
import random

heads = 0
tails = 0

def flipCoin():
  global heads, tails
  num = random.randint(0, 1)
  if num == 0:
    heads += 1
  else:
    tails += 1

for i in range(1000):
  flipCoin()

print(str(heads/10) + "% of your flips were heads.")
print(str(tails/10) + "% of your flips were heads.")

"""5 / 3 # -- always gives us a float
5 // 3 # --> gives us an integer
5.4 // 3.6 # gives us a float

#floor(2.999) --> 2"""