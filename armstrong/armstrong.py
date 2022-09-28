a = int(input("Enter the number: "))
sum = 0
#to get the order we need to calculate the length and create a string of that len
order = len(str(a))
b = a #assign the value of a so that it can be zero
while(a>0):
    digit = a%10
    sum = sum+digit**order
    a= a//10
if(sum==b):
    print("its an armstrong number")
else: 
    print("its not an armstrong number")
