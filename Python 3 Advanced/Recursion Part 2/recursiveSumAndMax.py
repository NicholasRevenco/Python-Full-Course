# main.py

#involves slicing to change the argument of the recursive call

def function(list_of_numbers, highest_number, sum_of_numbers, len_of_list_add_one):
  if len(list_of_numbers) > 0 and list_of_numbers[0] >= highest_number:
    highest_number = list_of_numbers[0]
  if len_of_list_add_one != 0:
    function(list_of_numbers[1:len(list_of_numbers)], highest_number, sum_of_numbers+list_of_numbers[0], len_of_list_add_one-1)
  else:
    return print(sum_of_numbers), print(highest_number)

function([1, 2, 50, 4, 5, 15], 0, 0, len([1, 2, 50, 4, 5, 15]))

def recursive_sum(l):
  if len(l) == 1:
    return l[0]
  return l[0] + recursive_sum(l[1:])
  
l = [1, 2, 3]
recursive_sum(l)
'''m = '''

def recursive_max(l):
  if len(l) == 1:
    return l[0]
  if l[1] > l[0]:
    return recursive_max(l[1:])
  else:
    return recursive_max(l[0:1] + l[2:])
    


print(recursive_max([3, 2, 1]))
print([1] + [2, 3])
  
#[2, 1, 5, 3, 4] --> [2, 5, 3, 4] --> [5, 3, 4] --> [5, 4] --> [5]
#[2, 1, 5, 3, 4} --> [1, 5, 3, 4] --> ...]

def add_two(x):
  x + 2
  
print("2 plus 4 is " + str(add_two(4)))