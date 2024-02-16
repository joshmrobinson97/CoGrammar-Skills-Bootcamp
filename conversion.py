"""

conversion.py pseudo code:

declare variables 1-4
assignment appropriate variable type
on each line, print the variable + type(variable)

"""

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100" #named variables

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1) #converted all variables to required variable type

print("str(num1) (" + str(num1) + ") is " + str(type(num1)))
print("str(num2) (" + str(num2) + ") is " + str(type(num2)))
print("str(num3) (" + str(num3) + ") is " + str(type(num3)))
print("str(string1) (" + str(string1) + ") is " + str(type(string1))) #added str() so that it can concatenate and named them for clarity
