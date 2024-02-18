"""menu.py psuedo-code

create a dictionary for menu
create a dictionary for stock
create a dictionary for price
create an empty string which can have the final value in it
loop for stock, price in menu

calculate items * price for each item and concatenate answer to final value
print final value
(option: add input values for all the items, stock, & price) """

menu = ["Chicken", "Rice & Peas", "Oxtail", "Dumplings"]

menu_stock = {"Chicken" : 100, 
"Rice & Peas" : 150,
"Oxtail" : 75,
"Dumplings" : 400
}

menu_price = {"Chicken" : 8.50,
"Rice & Peas" : 3.50,
"Oxtail" : 10.00,
"Dumplings" : 1.50,
}

total_stock = 0

for key in menu_price:
    total_stock += menu_price.get(key) * menu_stock.get(key)

print("\n\nThe available menu is \n" + str(menu))

print("-" * 30)

print("The price for each item is \n" + str(menu_price))

print("-" * 30)

print("The stock for each item is \n" + str(menu_stock))

print("-" * 30 + "\n")

print("You currently have £" + str(total_stock) + " of inventory.\n")

