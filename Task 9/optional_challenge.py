""" logic.py
write a program that contains a logical error 
create a input for a number between 1-50
use calculations to figure out what number you've chosen
"""

num = input("Please enter a number between 1-10: ")


if num,isdigit(): # Runtime error as it should be a dot instead of a comma
    # runtime error here as the input should be cast as an integer for the calculations to work.
    if 1 <= num and num <= 10:
        if num % 2 == 0:
            if num - 2 == 0:
                print("Your number is " + 2) # Runtime error here occurs because it cannot concatenate a string and an integer
        
            elif num % 3 == 1:
                if num % 5 == 0:
                    print("Your number is 10.")
                else:
                    print("Your number is 4.")

            elif num % 4 == 2:
                if num % 5 == 1:
                    print("Your number is 6.")
                else:
                    print("Your number is 8.")

        else:
            if num % 3 == 0:
                if num - 3 == 0:
                    print("Your number is 3.")
                else:
                    print("Your number is 9.")

            elif num % 3 == 2:
                print("Your number is 5.")

            elif num % 4 == 3:
                print("Your number is 7.")

            elif num + 1 == 0: # Logical error here as it should be minus 
                print("Your number is 1.")

    else; # Syntax error, the semi colon should be a colon
        print("Invalid input. Please enter a number between 1 and 10.")

else:
    print("Invalid input. Please enter a valid integer.")
