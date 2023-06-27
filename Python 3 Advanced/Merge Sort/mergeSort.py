# main.py

def merge(a, b):
  aIndex = 0
  bIndex = 0
  result = []
  while aIndex != len(a) and bIndex != len(b):
    if a[aIndex] < b[bIndex]:
      result.append(a[aIndex])
      aIndex += 1
    else:
      result.append(b[bIndex])
      bIndex += 1
  if aIndex != len(a):
    for i in range(aIndex, len(a), 1):
      result.append(a[i])
  elif bIndex != len(b):
    for i in range(bIndex, len(b), 1):
      result.append(b[i])
  
  return result

#print(merge([3, 8, 9], [1, 4, 5]))

def split(lst):
  if len(lst) <= 1:
    print(lst)
    return lst
  split(lst[:len(lst)//2])
  split(lst[len(lst)//2:])

#print(split([5, 4, 3, 2, 1, 10, 9]))

def mergeSort(lst):
  if len(lst) <= 1:
    return lst
  return merge(mergeSort(lst[:len(lst)//2]), mergeSort(lst[len(lst)//2:]))
  
print(mergeSort([5, 4, 3, 1, 9]))
  