# Declare an empty list
empty_list = list()

# Declare a list with more than 5 items
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
# Find the length of your list
print(len(fruits))
# Get the first item, the middle item and the last item of the list
print(fruits[0])
print(fruits[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types =['Jatin','24','173','Taken','Paris']


# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
# Print the list after modifying one of the companies
remove_company = it_companies.remove("Oracle")
print(it_companies)
# Add an IT company to it_companies
add_company = it_companies.insert(1,'Wottaspace')
print(add_company)
# Insert an IT company in the middle of the companies list
add_company1 = it_companies.insert(3, 'Newpickup')
print(add_company1)
# Change one of the it_companies names to uppercase (IBM excluded!)
new = [word.upper() for word in it_companies]
print(new)
# Join the it_companies with a string '#;  '
string1 = ['#;  ']
#add = it_companies.insert(0, string1)
add1 = it_companies+string1

print(add1)

# Check if a certain company exists in the it_companies list.
if('Newpickup' in it_companies):
    print("already exists")
else:
    print("not exists")

# Sort the list using sort() method
sorting = sorted(it_companies)
print(sorting)

# Reverse the list in descending order using reverse() method
sortingR = sorted(it_companies, reverse=True)
print(sortingR)
# Slice out the first 3 companies from the list
print(it_companies[0:3])
# Slice out the last 3 companies from the list
print(it_companies[-1:2])
# Slice out the middle IT company or companies from the list
len1 = len(it_companies)/2
# Remove the first IT company from the list
print(it_companies.pop(0))
# Remove the middle IT company or companies from the list

# Remove the last IT company from the list
print(it_companies.pop(-1))
# Remove all IT companies from the list
del it_companies
# Destroy the IT companies list

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullback = (front_end+back_end)
print(fullback)


# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = fullback.copy()
addfull = full_stack.insert(0,'Python')
addfull2 = full_stack.insert(1, 'SQL')
print(addfull)
print(addfull2)