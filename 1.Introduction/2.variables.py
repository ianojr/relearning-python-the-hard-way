# Variable - A container for a value(string, boolean, float, integer).
#  Variables behave as if it was the value it contains


# String - A series of Characters
first_name = "Bob"
food = "Pizza"
email = "fake@mail.com"

print(f"Your name is {first_name}")
print(f"You like {food}")
print(f"Your email is {email}\n")


# Integer
age = 20
quantity = 50
num_of_students = 120

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print("The total number of students in your class are", num_of_students)
print(" ")


# Float
price = 105.78
gpa = 3.9
distance = 23.56

print(f"The total price is ${price}")
print(f"You have a GPA of {gpa}")
print(f"He has walked a distance of {distance}km\n")




# Boolean
is_student = False
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")


if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")


if is_online:
    print("You are online")
else:
    print("You are offline")

print(" ")




# Assignment - Post 4 variables

user_name = "john_doe"
salary = 23.90
age = 45
is_online = False

print(f"Username is {user_name}")
print(f"The salary is {salary}")
print(f"The age is {age}")
print(f"Are you online?: {is_online}")

if is_online:
    print(f"{user_name} is online")
else:
    print(f"{user_name} is not online")