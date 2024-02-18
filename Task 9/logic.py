import math
# create a list of available options
shape_list = ["circle", "square", "rectangle", "triangle"]
print("\nThis programme will ask you to select from a list of shapes, ask for the dimensions and will calculate the area of said shape.\n")
shape = input(f"Please choose a shape:\nA reminder that the available shapes are {shape_list}.\n")

# Create the outcome should they choose circle
if shape == shape_list[0]:
    print("You chose circle")
    radius_circle = float(input("Enter the radius of the circle: "))
    # The mathematics for the area of a circle
    area_circle = math.pi * radius_circle ** 2
    print(f"The area of the circle is {area_circle}units^2")

# Create the outcome should they choose square
elif shape == shape_list[1]:
    print("You chose square")
    square_length = float(input("Enter the length of a side: "))
     # The mathematics for the area of a square
    area_square = square_length ** 2
    print(f"The area of the square is {area_square}units^2")

# Create the outcome should they choose rectangle
elif shape == shape_list[2]:
    print("You chose rectangle")
    rectangle_length1 = float(input("Enter one length of the rectangle: "))
    rectangle_length2 = float(input("Enter the other length of the rectangle: "))
     # The mathematics for the area of a rectangle
    area_rectangle = rectangle_length1 * rectangle_length2
    print(f"The area of your rectangle is {area_rectangle}units^2.")

# Create the outcome should they choose triangle
elif shape == shape_list[3]:
    print("You chose triangle")
    triangle_height = float(input("Enter the height of the triangle: "))
    triangle_base = float(input("Enter the base of the triangle: "))
     # The mathematics for the area of a triangle
    area_triangle = triangle_base * triangle_height / 2 # incorrect mathematics here. should be (triangle_base * triangle_height) / 2
    print(f"The area of the triange is {area_triangle}units^2")