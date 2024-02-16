"""numbers.py pseudo code

Ask for three seperate numbers through inputs
assign them each strings
covert each string to floats
maths:
  add all of them using sum()
  num1 - num2
  num3 * num1
  sum(nums) / num3
"""

num1 = float(input("Input a 1st number"))
num2 = float(input("Input a 2nd number"))
num3 = float(input("Input a 3rd number"))

print("Your numbers are {num1}, {num2}, & {num3}")

print("The sum of your numbers is: {}".format(sum([num1, num2, num3])))

print(num1 - num2)

print(num3 * num1)

print(sum([num1, num2, num3]) / num1)

