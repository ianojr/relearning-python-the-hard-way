# input() - A function that prompt the user to enter data
#      Returns the entered data as a string

name = input("What is your name?: ")
age = input("How old are you?: ")

# int(age) += 1
age = int(age) + 1

print(f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")