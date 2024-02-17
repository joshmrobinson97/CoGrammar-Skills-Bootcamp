""" while.py pseudo-code

set a total as 0
set a counter to 0
ask for an input of a number, assign num
create while statement
 while number doesn't equal -1
  total += num
  counter += 1
  ask for another input

  if num equals -1
  average = total / counter
  print average
  break loop """

total = 0
counter = 0

num = input("Enter a number. (Input -1 to break): ")

while not num.isdigit(): # checks to see whether the entered number is a digit
  num = input("Please enter a number for the program to work: ")

num = int(num) # casts the digit as an integer

while num == -1: # asks the user to enter a number that isn't -1
  num = int(input("You entered -1, please enter a different number: "))

while num != -1: # Continues as long as number is not -1
  total += num # For each loop the total increases by the number
  counter += 1 # For each loop the counter increases by 1
 
  num = int(input("Enter a number. (Input -1 to break): "))
  if num == -1:
    average = total / counter # create the average using mean = sum(x)/n
    print("\n" + "-" * 48)
    print("The average for all the numbers is equal to " + str(average) + ".")
    print("-" * 48)
    break # end the loop
