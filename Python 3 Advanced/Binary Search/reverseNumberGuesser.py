# main.py
print('Think of a whole nuber between 0 and 100, and I will guess it!')

def recursive(numbers, guess=0):
  guess += 1
  middle = len(numbers) // 2
  print_middle = numbers[middle]
  if guess > 7:
    return print('\nI do not think you answered one of the questions correctly....')
  user_input = input('\nGuess ' + str(guess) + ': Is your number ' + str(print_middle) + '?\nIf not, is it above or below ' + str(print_middle) + "?\nType 'yes', 'above', or 'below': ")
  if user_input == 'yes':
    return print_middle
  elif user_input == 'below':
    return recursive(numbers[:middle], guess)
  else:
    return recursive(numbers[middle:], guess)

print('\nI knew your number was ' + str(recursive(range(101))) + '!')

#O(log(n))