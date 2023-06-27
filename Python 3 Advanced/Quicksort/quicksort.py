# main.py

def partition(pivot, lst):
  larger = []
  lesser = []
  equal = []
  for number in lst:
    if number > pivot:
      larger.append(number)
    elif number < pivot:
      lesser.append(number)
    else:
      equal.append(number)
  return larger, lesser, equal

def quicksort(lst):
  n = len(lst)
  
  if n <= 1:
    return lst
    
  pivot = lst[0]
  
  great, less, eq = partition(lst, pivot)
  sortedLess = quicksort(less)
  sortedGreat = quicksort(great)
  
  return sortedLess + eq + sortedGreat


def partition(lst, low, high):
  i = (low-1)
  pivot = lst[high]
  for j in range(low, high):
    if lst[j] <= pivot:
      i = i+1
      lst[i], lst[j] = lst[j], lst[i]
  lst[i+1], lst[high] = lst[high], lst[i+1]
  return (i+1)

def quicksort(lst, low, high):
  if len(lst) == 1:
    return lst
  if low < high:
    pi = partition(lst, low, high)
    quicksort(lst, low, pi-1)
    quicksort(lst, pi+1, high)

lst = [10, 7, 8, 9, 1, 5]
n = len(lst)
quicksort(lst, 0, n-1)
print(lst)