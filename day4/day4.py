# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a= "Thirty "
b = "days "
c = "of "
d = "python."
print(a+b+c+d)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = "coding "
fo ="for "
al = "all"
print(coding+fo+al)
# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for all"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[0]) 
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
if(company.find("Coding")):
    print("coding is there")
else:
    print("coding is not there")
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
# Change Python for Everyone to Python for All using the replace method or other methods.
python = "Python for Everyone"
print(python.replace("Python for Everyone", "Python for All"))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
bigcompany = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(bigcompany.split(","))
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
# s = 'Python for Everyone'
# x = s.split(' ')
# for i in x:
#     print (i[0])
# Create an acronym or an abbreviation for the name 'Coding For All'.
se = 'Coding For All'
# xe = s.split(' ')
# for j in xe:
#     print (j[0])
# Use index to determine the position of the first occurrence of C in Coding For All.
elem= 'Coding'
index_post = se.index(elem)
print(f'First index of element "{elem}" in the list: ', index_post)
# Use index to determine the position of the first occurrence of F in Coding For All.
sub_string = 'F'
print("the first occurunce of F is : ",se.index(sub_string))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
string1 = "Coding For All People"
print(string1.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word = "You cannot end a sentence with because because because is a conjunction"
print("first occurrence of the word 'because is ", word.rfind('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("first occurrence of the word 'because", word.rindex("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word1 = "You cannot end a sentence with because because because is a conjunction"
print(word1[31:54])
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
word2 ="'You cannot end a sentence with because because because is a conjunction"
print("first occurrence of the word 'because is ", word2.rindex ('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(word.count("because")) #needs to be done

# Does ''Coding For All' start with a substring Coding?
word3 ="Coding For All"
print(word.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print(word.endswith('All'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
word4 = '   Coding For All      '
print(word4.strip())
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new = [' ', '#']
print(libraries + new)
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# Make the following using string formatting methods:

a1 = 8
b1 = 6


# 8 + 6 = 14
print('{} + {} = {}'.format(a1, b1, a1 + b1))
# 8 - 6 = 2
print('{} + {} = {}'.format(a1, b1, a1 - b1))
# 8 * 6 = 48
print('{} + {} = {}'.format(a1, b1, a1 * b1))
# 8 / 6 = 1.33
print('{} + {} = {}'.format(a1, b1, a1 / b1))
# 8 % 6 = 2
print('{} + {} = {}'.format(a1, b1, a1 % b1))
# 8 // 6 = 1
print('{} + {} = {}'.format(a1, b1, a1 // b1))
# 8 ** 6 = 262144
print('{} + {} = {}'.format(a1, b1, a1 ** b1))