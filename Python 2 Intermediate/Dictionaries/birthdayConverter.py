#Dictionaries needed
monthToString = {
  1: "January",
  2: "February",
  3: "March",
  4: "April",
  5: "May",
  6: "June",
  7: "July",
  8: "August",
  9: "September",
  10: "October",
  11: "November",
  12: "December"
}
daySuffix = {
  0: "th",
  1: "st",
  2: "nd",
  3: "rd",
  4: "th",
  5: "th",
  6: "th",
  7: "th",
  8: "th",
  9: "th"
}
#String needed
print_birthday = "You were born on "
#Variables needed
month = 0
day = 0
#User input
user_birthday_input = input("Enter your birthday in the form, 'mm/dd/yyyy' (add 0 to the beginning of the month or day if it is single digit number): ")
#Month converted from input
if user_birthday_input[0] == "0":
  month = int(user_birthday_input[1])
else:
  month = int(user_birthday_input[0] + user_birthday_input[1])
print_birthday += monthToString[month] + " "
#Suffix for the day from the input
suffix = int(user_birthday_input[4])
if user_birthday_input[3] != "0":
  day = user_birthday_input[3] + user_birthday_input[4]
elif user_birthday_input[3] == "0":
  day = user_birthday_input[4]
if day == "11" or day == "12" or day == "13":
  suffix = 9
#Add the day and the year to the final print
print_birthday += day + daySuffix[suffix] + ", " + user_birthday_input[6]+ user_birthday_input[7]+ user_birthday_input[8] + user_birthday_input[9]
#Print the converted user's input
print("\n" + print_birthday)