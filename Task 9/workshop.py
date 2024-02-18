""" logic.py
write a program that contains a logical error 
create a input for a number between 1-50
use calculations to figure out what number you've chosen
"""

num = input("Please enter a number between 1-10: ")


if num.isdigit():
    if 1 <= num <= 10:
        num = int(num)
        if num % 2 == 0:
            if num - 2 == 0:
                print("Your number is 2.")
        
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

            elif num - 1 == 0:
                print("Your number is 1.")
    else:
        print("Invalid input. Please enter a number between 1 and 10.")

else:
    print("Invalid input. Please enter a valid integer.")
