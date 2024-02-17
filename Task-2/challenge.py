""" challenge.py
declare what I will seek to accomplish
ask for three separate lengths
name them each side1, side2, & side3
use formula
 s=(side1+side2+side3)/2and
 area = √(s(s-a)*(s-b)*(s-c))
print area
"""

print("This is a program where I will seek to display the area of a triangle whose sides you've quantified.\nThe results will be shown below.")

side1 = float(input("Give the first side of the triangle: "))
side2 = float(input("Give the second side of the triangle: "))
side3 = float(input("Give the first side of the triangle: "))

print(f"Your lengths are {side1}, {side2}, & {side3}")

s = (side1 + side2 + side3) / 2
area = ((s * (s - side1) * (s - side2) * (s - side3)) ** 0.5)

print(f"The area of your triangle is {area} units^2")
