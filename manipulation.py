"""manipulation.py psuedo code

Create an input for use to type sentence
display how many characters it has
create a new string which isolates the last character
 display that string
repeat line 5 isolating the last 3 letters (use -1 step)
 display reverse string
create a new string which isolates the first 3 characters
create a separate string which isolates the last 2 characters
 display them combined to create new word

"""

str_manip = input("Enter a sentence: ")
print("This sentence has {} characters".format(len(str_manip)))

last_letter = str_manip[-1]
print(str_manip.replace(last_letter, "@"))

final_letters = str_manip[-1:-4:-1]

print(f"The last three characters in reverse are: {final_letters}")

first_three_letters = str_manip[:3]
last_two_letters = str_manip[-2:]

print(f"Your created word is {first_three_letters}{last_two_letters}.")
              
