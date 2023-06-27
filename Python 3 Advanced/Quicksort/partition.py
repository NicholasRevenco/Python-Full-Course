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
  