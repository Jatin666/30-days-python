number = int(input("enter the number: "))
reverse = 0
a = number
while(number>0):
    digit = number%10
    reverse = reverse*10+digit
    number = number//10
if(a==reverse):
    print("number is palidrome")
elif(a==0 and a<0):
    print("enter correct number")
else:
    print("its not an palindrome")