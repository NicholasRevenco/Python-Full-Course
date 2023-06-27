# main.py

def split(lst):
  if len(lst) <= 1:
    print(lst)
    return lst
  split(lst[:len(lst)//2])
  split(lst[len(lst)//2:])

print(split([5, 4, 3, 2, 1, 10, 9]))