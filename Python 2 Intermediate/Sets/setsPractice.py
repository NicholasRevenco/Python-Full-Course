# main.py
import random
#All of the sets needed
first_set = set()
second_set = set()
user_set = set()
user_set2 = set()
numbers = set()
even_numbers = set()
words = set()
three_lettered_words = set()
#Print different things about the random numbers in first_set and second_set
for i in range(5):
  random_number = random.randint(1, 10)
  random_number2 = random.randint(1, 10)
  first_set.add(random_number)
  second_set.add(random_number2)
print(first_set)
print(second_set)
print(first_set.union(second_set))
print(first_set.intersection(second_set))
#Print out if the second_set has the number one
if 1 in second_set:
  print("The number 1 is inside the second set.")
else:
  print("The number 1 is not inside the second set.")
#Print the unique letters in the user's word and the amount of unique letters in the word
user_word = input("Give me a word: ")
for letter in user_word:
  user_set.add(letter)
print(user_set)
print("This word has " + str(len(user_set)) + " unique letters.")
#Print the user's second input intersected with the user's first input
user_word2 = input("Give me another word: ")
for letter in user_word2:
  user_set2.add(letter)
print(user_set.intersection(user_set2))
#Print even numbers in a set of numbers
for i in range(1, 10, 1):
  numbers.add(i)
def find_even_numbers(set_numbers):
  for number in set_numbers:
    if number % 2 == 0:
      even_numbers.add(number)
  return even_numbers
print(find_even_numbers(numbers))
#Print words that have 3 letters in them
words.add('buffalo')
words.add('dog')
words.add('cat')
words.add('eagle')
words.add('bear')

for word in words:
  if len(word) == 3:
    three_lettered_words.add(word)
print(three_lettered_words)