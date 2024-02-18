# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # added brackets () to the print command
print("\n") # fix indentation and added brackets () to the print command

# Variables declaring the user's age, casting the str to an int, and printing the result
'''age_Str = "24" # removed one = to allow age_Str to be defined. Removed "years old" to allow 24 to be casted as a string '''
age = 24 # removed age_Str and added the value 24 as a pure integer so total years (line 15) can concatenate easier
print("I'm " + str(age) + " years old.") # casted the now integer "age" as string so it can concatenate. Added space next to "I'm"

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # removed the "" so it can concatenate
total_years = age + years_from_now

print("The total number of years: " + str(total_years)) # added brackets () to the print command. Removed brackets off answer_years, renamed age, and casted string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 # renamed total to total_years and added 6 addition months. 
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # added brackets () to the print command. casted total_months as string so it will concatenate

#HINT, 330 months is the correct answer

