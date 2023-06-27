import random

def bubbleSort(lst):
  for i in range(len(lst)):
    for i in range(len(lst)-1):
      if lst[i] > lst[i+1]:
        old_number = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = old_number
  return lst

print(bubbleSort([5000, 2, 360, -4, 9000, 67]))

#[5, 4, 10]