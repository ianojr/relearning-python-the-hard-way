# Write a python code that displays a listing of a Real Estate appartment and the core details


apartment_name = "Genesis Groove"
floors = 23
rent_per_month = 100000.50
max_capacity_reached = True

print(f"The apartment name is {apartment_name}")
print(f"It has {floors} floors")
print(f"The rent per month is ksh{rent_per_month}")

if max_capacity_reached:
    print("There is no Vacant room")
else:
    print("There are vacant room available")