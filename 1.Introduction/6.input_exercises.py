# Exercise 1 - Calculate the area of a rectangle
length = float(input('Enter the length: '))
width = float(input('Enter the width: '))

area = length * width

print(f"The area is {area}cm²\n")




# Exercise 2 - A shopping cart program that accepts an item, price and the quantity
item = input("What do u want to buy?: ")
quantity = int(input("What is the quantity?: "))
price = float(input("What is the price for one item?: "))

total = price * quantity
print(f"You have bought {quantity} {item}/s at a price of ${total}")