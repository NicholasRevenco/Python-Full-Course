# main.py
import time
from random import randint

#Different functions
def linear_serach(numbers, target):
  for i in range(len(numbers)):
    if numbers[i] == target:
      return True
  return False

def recursive(numbers, target):
  middle = len(numbers) // 2
  if numbers[middle] == target:
    return True
  elif len(numbers) == 1:
    return False
  elif numbers[middle] > target:
    return recursive(numbers[:middle], target)
  else:
    return recursive(numbers[middle:], target)

#Search time variables
time_total_linear_serach = 0
time_total_binary = 0
#Creating the random list to search from
random_list = []
for i in range(10000):
  random_list.append(randint(0, 100000))
random_list.sort()
#Linear search time for 1000 integers
print('Starting linear search...')
for i in range(1000):
  start_time = time.time()
  linear_serach(random_list, randint(0, 100000))
  time_total_linear_serach += time.time()-start_time
print('Linear search ended.')
#Binary search time for 1000 integers
print('Starting binary search.')
for i in range(1000):
  start_time = time.time()
  recursive(random_list, randint(0, 100000))
  time_total_binary += time.time()-start_time
print('Binary search ended.\n')
#Print statements of the times
print('Linear search time: ' + str(time_total_linear_serach) + ' seconds')
print('Binary search time: ' + str(time_total_binary) + ' seconds')