# main.py

def ifParenthesesIterative(string):
  stack = []
  dictionary = {'(': ')', '[': ']', '{': '}'}
  for parentheses in string:
    if parentheses == '(' or parentheses == '[' or parentheses == '{':
      stack.append(parentheses)
    elif len(stack) == 0:
      return print("False")
    elif dictionary[stack.pop()] != parentheses:
      return print("False")
  return print("True")

ifParenthesesIterative("[({})]")

# ([]{}). ([{}]), {[(]}, ([)], ([]...), [{}([])], ({})([]), #)()

# 4! = 4 * 3 * 2 * 1, 4! = 4 * 3!
# [({})] --> (valid) --> this is also a valid string
#valid = ({}) = (valid)
#base case: "()" or "[]" or "{}"
# 'a'
# zracecarzbb


#[ ( ) ] [ ] --> [][] -- > [] -- > valid


#{()[()]} --> {()[]} --> {[]} --> {} --> valid
# (3 + (4 - (2 * 3))) + 5 --> (3 + (4 - 6)) + 5 --> (3 - 2) + 5 --> 1 + 5--> 6

#hello -> len = 5 -> range = 0, 1, 2, 3, 4
#i=0 -> string[0] + string[1]
#i=1 -> string[1] + string[2]
#i=4 -> string[4] + string[5]
def ifParenthesesRecursive(string):
  dictionary = {'(': ')', '[': ']', '{': '}'}
  
 
  for i in range(len(string)-1):
  
    
    p = string[i] + string[i+1]
    
    if p == '()' or p == '[]' or p == '{}':
      if len(string) == 2:
        print("DEBUG")
        return True

      #remove the valid characters from the string
      newString = string[:i] + string[i+2:]
      return ifParenthesesRecursive(newString)
      #[]
      
  return False
      
      
  """if len(string) < 2:
      return print("False")
  if parentheses == ")" or parentheses == "]" or parentheses == "}":
    if dictionary[string[x-2]] == parentheses:
      string = string[:x-2] + string[x:]
      print("SomethingHere")
      ifParenthesesRecursive(string, 0)
    else:
      return print("False")"""

print(ifParenthesesRecursive("{[()][]{}}"))

#Problems: sometimes there are two printed answers, there is allways an error message after giving the right answer because you can't cut into a two length string the same way you cut into a four length string

'''my_list = [1, 4, 6, 3]

stack = [4, 1, 2]
a = stack.pop()
print(a)
print(stack)
stack.append(5)
'''
