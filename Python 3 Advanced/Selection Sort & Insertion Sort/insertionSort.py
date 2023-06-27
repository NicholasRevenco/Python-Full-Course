# main.py

# [5, 2, 3, 1, 4]
# []
# [5] 
# [5, 2] -> [2, 5]
# [2, 5, 3] -> [2, 3, 5]
# [2, 3, 5, 1] -> [1, 2, 3, 5]

'''def insertionSort(lst, new_lst=[]):
  for i in range(len(lst)):
    new_lst.append(lst[i])
    if len(new_lst) > 1:
      for j in range(i, 0, -1):
        if new_lst[j] < new_lst[j-1]:
          old_place = new_lst[j]
          new_lst[j] = new_lst[j-1]
          new_lst[j-1] = old_place
  return new_lst

print(insertionSort([5, 4, 3, 2, 1]))'''



def insertionSort(lst):
  for i in range(len(lst)):
    for j in range(i, 0, -1):
      if lst[j] < lst[j-1]:
        swap()
        old_place = lst[j]
        lst[j] = lst[j-1]
        lst[j-1] = old_place
  return lst


print(insertionSort([5, -10, 9, 2, 3, -100, 1324]))