# main.py

word = input("Enter a word: ")
index = input("Enter an index: ")
print("The word you entered was " + word)
print("The letter at index " + index + " of '" + word + "' is '" + word[int(index)-1] + "'")