# Declare your age as integer variable
age = 24
# Declare your height as a float variable
height1 = 175.6
# Declare a variable that store a complex number
complex_number = 1 + 1j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = (base*height)*0.5
print ("The area of the triangle is :" , area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
side_a = int(input("enter side a"))
side_b = int(input("enter side b"))
side_c = int(input("enter side c"))
perimetere = side_a+side_b+side_c
print("the perimeter of the triangle is :" , perimetere)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("enter the length of rectangle: "))
width = int(input("enter the width of rectangle: "))
print("the area of rectangle is : ", length*width)
print("the perimetre of rectangle is:  ",  2 * (length + width))
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = int(input("Enter radius: "))
print("the area of circle: ",pi * r * r)
print("the circumfrence of circle: ", 2 * pi * r)
# Calculate the slope, x-intercept and y-intercept of y = 2x -2



# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)


# Compare the slopes in tasks 8 and 9.


# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
a = "python"
b = "dragon"
if (len(a)== len(b)):
    print("Length is same")
else:
    print("length is not same")
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if('on' in a):
    print("there is on present")
else:
    print("there is no ")
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
s = "I hope this course is not full of jargon."
if("jargon" in s):
    print("Jargon is present")
else:
    print("Jargon is not present")
# Find the length of the text python and convert the value to float and convert it to string

#s = "I hope this course is not full of jargon."
lenght = len(s)
conversion = print(float(lenght))
conversion2 = print(str(lenght))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
even = int(input("Enter the number: "))
if((even/2) == 0):
    print("this is even")
else:
    print("this is not even")
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
float1 = 2.7
conversion_to_int = int(float1)
if(7//3 == conversion_to_int):
    print("its equal")
else:
    print("its not equal")
# Check if type of '10' is equal to type of 10
type1 = '10'
type2 = 10
if(type(type1)==type((type2))):
    print("type is equal")
else:
    print("type is not equal")
# Check if int('9.8') is equal to 10
int1 = int(9.8)
int2 = 10
if (int1== int2):
    print("int is equal to 10")
else:
    print("int is not equal to 10")
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
hours = int(input("Enter the hours: "))
rate = int(input("Enter the rate per hour: "))
print("Your weekly earning is: ", hours*rate)
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Enter number of years you have lived: 100
# You have lived for 3153600000 seconds.
year= int(input("Enter number of years you have lived: "))
second_person_can_live = 31536000
print("You have lived for", year , "seconds")
# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
