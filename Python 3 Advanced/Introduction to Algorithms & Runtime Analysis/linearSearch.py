# main.py

#Algorithms:
#step-by-step process to do something
#comparing algorithms:
# 1) speed/time 
# 2) space/efficiency
# if num in lst

def function(list1, value):
  for number in list1:
    if number == value:
      return True
  return False

print(function([1, 2, 3, 4, 5], 0))