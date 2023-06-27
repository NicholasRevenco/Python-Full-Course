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

print(merge([3, 8, 9], [1, 4, 5]))