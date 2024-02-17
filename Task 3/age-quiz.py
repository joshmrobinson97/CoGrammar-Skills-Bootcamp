""" age-quiz.py pseudo code
Ask for an age input and store it as a integer variable
create a initial if statement for whether patient is over 40 displaying info
use elif for if someone is over 100 displaying message
use elif for if someone is above 65 and under 99 to display message
use elif for if under 13 and output message
use elif if age is exactly 21 and display number
use else for final message
"""

age = input("Please enter your age: ")

# Check if a variable is a digit and loops until complete

while not age.isdigit():
  age = input("Please enter a number for your age: ")


else:
  age = int(age) # cast the digit as an integer

  # Check if a digit is above 0 and loops until complete
  while age < 0:
    age = int(input("Please enter a non-negative number: "))

  else:
    if age > 100:
      print("Sorry, you're dead.")
    elif age >= 65 and age <= 100:
      print("Enjoy your retirement!")
    elif age >= 40 and age < 65:
      print("You're over the hill.")
    elif age == 21:
      print("Congrats on your 21st!")
    elif age < 13:
      print("You qualify for the kiddie discount.")
    else:
      print("Age is but a number.")