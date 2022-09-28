# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
maxlist =[]
minlist =[]
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
max =sorted(ages)
list_add = maxlist.append(max)
print(maxlist)
min = sorted(ages,reverse=True)
list_add1 = minlist.append(min)
print(minlist)

# Find the median age (one middle item or two middle items divided by two)
if(len(min)%2!=0):
    m = int((len(min)+1)/2-1)
    print(min(m))
else:
    m1 = int(len(min)/2-1)
    m2 = int(len(min)/2)
    print(min[m1]+min[m2]/2)
    
# Find the average age (sum of all items divided by their number )
avg = sum(ages)/len(ages)
print(avg)
# Find the range of the ages (max minus min)

# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.