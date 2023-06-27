# main.py

#[9, 5, 7, 2, 1]
#[1, 5, 7, 2, 9]
#[1, 2, 9, 5, 7]
#[1, 2, 5, 9, 7]
#[1, 2, 5, 7, 9]

def function(list, sorted_list=[], loop_around=-1):
  while sorted_list != list:
    loop_around += 1
    min_element = list[len(list)-1]
    track_index = len(list)-1
    for i in range(loop_around, len(list), 1):
      if list[i] < min_element:
        min_element = list[i]
        track_index = i
    list[track_index] = list[loop_around]
    list[loop_around] = min_element
    sorted_list.append(min_element)

function([-5, 1, 3, 9, 1, 10, 1324])

'''def selectionSort(lst):
  result = []
  for i in range(len(lst)):
    minItem = lst[0]
    for item in lst:
      if item < minItem:
        minItem = item
      #minItem = min(minItem, item)
    result.append(minItem)
    lst.remove(minItem)
  return result
  
print(min(10, 4, 1))'''

def selectionSort(lst):
  for i in range(len(lst)):
    minItem = lst[0]
    for j in range(len(lst)-i):
      if lst[j] < minItem:
        minItem = lst[j]
    lst.remove(minItem)
    lst.append(minItem)
  return lst

print(selectionSort([4, 1, 10, -5, 0,  100, 21, -100, 3, 3, -9]))