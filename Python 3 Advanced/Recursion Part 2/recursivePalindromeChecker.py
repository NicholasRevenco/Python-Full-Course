# main.py
user_input = input("Enter the string you would like to check.\nWe will check if it a palindrome.\n")

def isPalindrome(string):
  if len(string) < 1:
    return True
  elif string[0] == string[-1]:
    palindrome(string[1:-1])
  else:
    return False

if isPalindrome(user_input):
  ...
  