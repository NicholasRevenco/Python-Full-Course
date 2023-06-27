# main.py

#Print welcome message
#Ask user for a username and a password for that username
#Ask either to make a deposit, a withdrawl, change the password, or to log out
#One dictionary would store the amount of money each user has
#Another dictionary would store the password of each user
#If the user's input is 1, ask the user how much to deposit, and add that number to the total amount of money they have
#If the user's input is 2, ask the user how much to withdrawl, and subtract that number to the total amount of money they have
#If the user does not have enough money that they want to withdrawl, print the user is unable to withdrawl that amount
#If the user's input is 3, ask the user for their current password, and then ask the user for the new password, to then replace the old password
#If the user's input is 4, exit the stop printing the messages

all_passwords = {"Nicholas Revenco" : "Password"}
all_money = {"Nicholas Revenco" : 0}

print("Welcome to the bank! Please log in.")
username = input("\nUsername: ")
password = input("Password: ")

if all_passwords[username] == password:
  while True:
    print("\nWelcome " + username + "! You currently have $" + str(all_money[username]) + " in your account. What would you like to do?\n  1.  Make a deposite\n  2.  Make a withdrawl\n  3. Change password\n  4.  Log out")
    action = int(input("What would you like to do: "))
    if action == 1:
      deposit = int(input("How much would you like to deposite? "))
      all_money[username] += deposit
    elif action == 2:
      withdrawl = int(input("How much would you like to withdrawl? "))
      if withdrawl <= all_money[username]:
        all_money[username] -= withdrawl
      else:
        print("You are unable to withdrawl that amouont of money.")
    elif action == 3:
      old_password = input("Please type in your current password: ")
      if old_password == all_passwords[username]:
        new_password = input("Please tye in your new password: ")
        all_passwords[username] = new_password
      else:
        print("Your password is not correct")
    else:
      break