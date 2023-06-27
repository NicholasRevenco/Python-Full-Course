# main.py

def linear_search(numbers, target):
  for i in range(len(numbers)):
    if numbers[i] == target:
      return True
  return False

print(linear_search([1,2,3,4,5,6,7], 0))

#Do not remember doing this:
'''def recursive1(numbers, target):
  if len(numbers) == 0:
    return False
  if numbers[0] == target:
    return True
  return recursive1(numbers[1:], target)

print(recursive1([1, 2, 3, 4, 5, 6], 4))'''

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

print(recursive([1, 5, 7, 10], 5))

#Do not remember doing this:
'''def recursive(numbers, target):
  while True:
    middle = len(numbers) // 2
    if len(numbers) == 1 and numbers[0] != target:
      return False
    elif numbers[middle] == target:
      return True
    elif numbers[middle] > target:
      numbers = numbers[:middle]
    else:
      numbers = numbers[middle:]

print(recursive([-1, 5, 6, 7, 10], 3))'''
