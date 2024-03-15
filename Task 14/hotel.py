""" hotel.py pseudo code
test
calculate user's total holiday cost
plane cost, hotel cost, & rental cost (potentially give options)
city_flight options
num_flights is stored as integer
rental days stored as integer 

four functions:
    hotel_cost takes num_night and returns amount 
    plane_cost takes city_flight and returns amount
    car_rental takes rental_days and returns amount
    holiday_cost is the total of it all

print it all out in a presentable way"""

def hotel_cost(hotel_nights, h_price):
    
    total_hotel = hotel_nights * h_price
    return(total_hotel)

def plane_cost(vol, f_class):

    total_flight = vol * f_class
    return(total_flight)

def car_rental(rental_days):

    total_car = rental_days * 250
    return(total_car)

def holiday_cost(hotel_cost, plane_cost, car_rental):

    total_holiday = hotel_cost + plane_cost + car_rental
    return(total_holiday)

#------------------------------------------------------

# plane_cost

location = input("\nPlease enter the number corresponding with the flight destination:\n\n(1) Hồ Chí Minh City - £700\n(2) Dundee, Scotland - £350\n(3) Jackson, Mississippi - £800\n\n")

while not location.isdigit(): # ensures the number is a digit
    location = input("\nPlease enter a number corresponding with the flight destination:\n\n(1) Hồ Chí Minh City - £700\n(2) Dundee, Scotland - £350\n(3) Jackson, Mississippi - £800\n\n")

else:
    
    location = int(location)

    while location < 0 or location > 3: # Ensures the number is within the correct range
        location = int(input("\nPlease enter a valid number corresponding with the flight destination:\n\n(1) Hồ Chí Minh City - £700\n(2) Dundee, Scotland - £350\n(3) Jackson, Mississippi - £800\n\n"))
    else:
        if location == 1:
            city_flight = 700
            place = "Hồ Chí Minh City"
           

        elif location == 2:
            city_flight = 350
            place = "Dundee, Scotland"
            

        elif location == 3:
            city_flight = 800
            place = "Jackson, Mississippi"
            

print("\n" + "__" * 30)
flight_class = input(f"\nPlease enter the number corresponding with the desired cabin class to {location}:\n\n(1) Economy\n(2) Economy Premium\n(3) Business\n(4) First\n\n")
while not flight_class.isdigit(): # ensures the number is a digit
    flight_class = input(f"\nPlease enter a number corresponding with the desired cabin class to {location}:\n\n(1) Economy\n(2) Economy Premium\n(3) Business\n(4) First\n\n")

else:
    flight_class = int(flight_class)

    while flight_class < 0 or flight_class > 4: # Ensures the number is within the correct range
        flight_class = int(input(f"\nPlease enter a valid number corresponding with the desired cabin class to {location}:\n\n(1) Economy\n(2) Economy Premium\n(3) Business\n(4) First\n\n"))
    else:
        if flight_class == 1:
            flight_class_multiplier = 1.0
            desired_class = "Economy"
        elif flight_class == 2:
            flight_class_multiplier = 1.3
            desired_class = "Premium Economy"
        elif flight_class == 3:
            flight_class_multiplier = 3.0
            desired_class = "Business"
        elif flight_class == 4:
            flight_class_multiplier = 3.7
            desired_class = "First Class"

flight_price = plane_cost(city_flight, flight_class_multiplier)

#------------------------------------------------------

# choosing hotel

print("\n" + "__" * 30)
hotel_choice = input(f"\nPlease enter the number corresponding with the hotel you want to stay in during your stay to {location}:\n\n(1) Shangri-la - £150/night\n(2) Best Western - £45/night\n(3) Marriott Hotel - £85/night\n(4) Cheapest local choice - £15\n\n")
while not hotel_choice.isdigit(): # ensures the number is a digit
    hotel_choice = input(f"\nPlease enter a number corresponding with the hotel you want to stay in during your stay to {location}:\n\n(1) Shangri-la - £150/night\n(2) Best Western - £45/night\n(3) Marriott Hotel - £85/night\n(4) Cheapest local choice - £15\n\n")

else:
    hotel_choice = int(hotel_choice)

    while hotel_choice < 0 or hotel_choice > 4: # Ensures the number is within the correct range
        hotel_choice = input(f"\nPlease enter the number corresponding with the hotel you want to stay in during your stay to {location}:\n\n(1) Shangri-la - £150/night\n(2) Best Western - £45/night\n(3) Marriott Hotel - £85/night\n(4) Cheapest local choice - £15\n\n")
    else:
        if hotel_choice == 1:
            hotel_price = 150
            hotel_name = "Shangri-la"
        elif hotel_choice == 2:
            hotel_price = 45
            hotel_name = "Best Western"
        elif hotel_choice == 3:
            hotel_price = 85
            hotel_name = "Marriott"
        elif hotel_choice == 4:
            hotel_price = 15
            hotel_name = "Cheapest local choice"

# num_night

print("\n" + "__" * 30)
num_night = input("\nHow many nights will you be staying in a hotel: ")

while not num_night.isdigit(): # ensures the number is a digit
    num_night = input("\nPlease enter a valid number: ")

else:
    num_night = int(num_night)

    while num_night < 0:
        num_night = int(input("\nPlease enter a number greater than or equal to 0: "))

    else:
        hotel_price = hotel_cost(num_night, hotel_price)
        print(hotel_price)


# ---------------------------------------------------

# rental_days

print("\n" + "__" * 30)

rental_choice = input(f"(Y/N) Do you plan on hiring a car whilst you're in {place}?\n\n").lower() # Makes the entered option lowercase to help with option selection

while rental_choice != "y" and rental_choice != "n": # Ensures the user enters the correct option
    rental_choice = input("Please enter a valid response.\nReminder that the options are Y for yes and N for no.\n\n").lower()

else:

    if rental_choice == "y":

        rental_days = input("\nHow many days will you be hiring a car for: ")

        while not rental_days.isdigit():
            rental_days = input("\nPlease enter a valid number: ")

        else:
            rental_days = int(rental_days)

            while rental_days < 0:
                rental_days = int(input("\nPlease enter a number greater than or equal to 0: "))

            else:
               car_price = car_rental(rental_days)
               print(car_price)

    else:
        car_price = car_rental(0)
        print(car_price)


# ----------------------------------------------------

# total price

total_holiday_price = holiday_cost(car_price, flight_price, hotel_price)

print(f"For your trip to {location}, it will cost a grandtotal of £{total_holiday_price}. The breakdown of costs are as follows:")
print("__" * 30)
print(f"Flights: £{flight_price} in {desired_class}\nAccomodation: £{hotel_price} and the {hotel_name}")
if rental_choice == "y": # Only is shown if the user opts to rent a car
    print(f"Car Rental: £{car_price}")
print("--" * 30)