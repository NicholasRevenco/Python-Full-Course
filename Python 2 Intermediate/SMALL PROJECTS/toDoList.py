# main.py

#Print welcome message
#In a while loop, print three options that the user will do with the to-do list
#Ask the user for an inupt from one of the three options
#If the user's input is one, ask the user for an input to add to the to-do list
#If the user's input is two, ask the user for an input to remove from the to-do list
#If the user's input is three, print the final message of the to-do list
#After the user inputs one to-do item, print all of the items in the to-do list

user_list_print = "\nHere is your updated list:"
user_list = []
number = 0

print("Welcome to your to-do list!\n")

while number == 0:
  print("What would you like to do with your to-do list?\n  1.  Add a task\n  2.  Remove a task\n  3.  Exit")
  input_number = input("Type in the number here: ")
  if input_number == "1":
    add_user_task = input("Please type in the task you would like to add: ")
    user_list.append(add_user_task)
  elif input_number == "2":
    remove_user_task = int(input("Please type in the number of the task you would like to remove: "))
    user_list.remove(user_list[remove_user_task-1])
  else:
    number = 1
  print(user_list_print)
  for i in range(1, len(user_list)+1, 1):
    print("  " + str(i) + ".  " + user_list[i-1])
  print("\n")