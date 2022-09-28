#excerise1  --------------Level 1
#Check the python version you are using
#command Python --version

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
# subtraction(-)
# multiplication(*)
# modulus(%)
# division(/)
# exponential(**)
# floor division operator(//)

print(3+4) #addtion
print(3-4) #subtraction
print(3*4) #multiplication
print(3%4) #modulus
print(3/4) #division
print(3**4) #expoential
print(3//4) #floor division operator

# Write strings on the python interactive shell. The strings are the following:

#answer: you just need to use single inverted comma

# 'Your name'  
# 'Your family name'
# 'Your country'
# 'I am enjoying 30 days of python'

# Check the data types of the following data:
# 10
# 9.8
# 3.14
# 4 - 4j
# ['Asabeneh', 'Python', 'Finland']
# Your name
# Your family name
# Your country

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Jatin"))
print(type("Kant"))
print(type("India"))

#----------------------------------------Level2----------------------------------------------------------------------------------------------------------------------

# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# Find an Euclidian distance between (2, 3) and (10, 8)

print(1)
print(3.14)
print( 3- 2j)

import math
print("Euclidian distance")
p1 = (2,3)
p2=(10,8)
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
print(distance)
