# Write a python comment saying 'Day 2: 30 Days of python programming'
#Declare a first name variable and assign a value to it
first_name = "jatin"
# Declare a last name variable and assign a value to it
last_name = "kant"
# Declare a full name variable and assign a value to it
full_name = "jatin kant"
# Declare a country variable and assign a value to it
country = "india"
# Declare a city variable and assign a value to it
city = "dagshai"
# Declare an age variable and assign a value to it
age = 6
# Declare a year variable and assign a value to it
year = 7
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = True
# Declare multiple variable on one line
a , b = 4, 8

# #------------------------------------------------Level2_----------------------------------------------------------------
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))

# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
if (len(first_name)== len(last_name)):
    print("lenght is equal")
else:
    print("lenght is not equal")
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# Add num_one and num_two and assign the value to a variable total
total = print(num_one+num_two)
# Subtract num_two from num_one and assign the value to a variable diff
diff = print(num_one-num_two)
# Multiply num_two and num_one and assign the value to a variable product
product = print(num_one*num_two)
# Divide num_one by num_two and assign the value to a variable division
division = print(num_one/num_two)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = print(num_one%num_two)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = print(num_one**num_two)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = print(num_one//num_two)
# The radius of a circle is 30 meters.
radius_of_circle = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
from math import pi
area_of_circle = print("The area of the circle with radius " + str(radius_of_circle) + " is: " + str(pi * radius_of_circle**2))
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = print("The circumfrence of the circle with radius " + str(radius_of_circle) + " is: " + str(pi * radius_of_circle*2))
# Take radius as user input and calculate the area.
user = int(input("enter the radius: "))
print(print("The circumfrence of the circle with radius " + str(user) + " is: " + str(pi * user*2)))
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user2 = input("enter the first name: ")
print(user2)
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords