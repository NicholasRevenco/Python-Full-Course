# main.py
word = "programing"
encrypted_word = []
string_encrypted_word = ""
number = 15
nothing = 0

def convert(guess):
  global encrypted_word
  for i in range(0, len(word), 1):
    if word[i] == guess:
      encrypted_word[i] = guess
  return encrypted_word

def print_encrypted_word(list_input):
  global string_encrypted_word
  for i in range(0, len(convert(guess)), 1):
    string_encrypted_word += list_input[i] + " "
  return string_encrypted_word

print("Welcome to the Wheel of Fortune! You have 15 guesses to gigure out the word. Good luck!")
for i in range(0, len(word), 1):
  encrypted_word.append('_ ')
  string_encrypted_word += encrypted_word[i]
print('\n' + string_encrypted_word + '\n')

while number != 0:
  string_encrypted_word = ""
  guess = input("Guess a letter! You have " + str(number) + " guesses remaining: ")
  print(print_encrypted_word(encrypted_word) + '\n')
  number -= 1
  if "_" in string_encrypted_word:
    nothing += 1
  else:
    print("You have won!")
    break
if number == 0 and nothing == 15:
  print("You have lost!")