# Typecasting - The process of converting a variable from one type to another
#              str(), int(), bool(), float()
# A user input is always a string

name = "James Andrew"
age = 24
gpa = 3.4
is_student = True


print(type(name)) # <class 'str'>
print(type(age)) # <class 'int>
print(type(gpa)) # <class 'float'>
print(type(is_student)) # <class 'bool'>
print("")


gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
print(age)

name = ""
print(bool(name)) # Can be used to check if the user entered a value or not


data = input("Type anything: ")
while not bool(data):
    data = input("Ensure u type anything: ")
