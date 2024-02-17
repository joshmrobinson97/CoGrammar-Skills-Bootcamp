"""
details.py psuedo code

create input asking for user's name
store string as name
create input asking for user's age
store string as age
create input asking for user's house number
store string as house_number
create input asking for user's Street name
store string as street_name

print sentence including the concatenation of the multiple strings
be sure that age and house_number are converted to strings using str() tool

"""

name = input("Please enter your name: ")
age = input("Please enter your age: ")
house_number = input("Please enter your House number: ")
street_name = input("Please enter your Street name: ")

print("This is " + name + ". He is " + str(age) + " years old and lives at " + str(house_number) + " " + street_name)
