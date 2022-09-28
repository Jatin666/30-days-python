#factorial of an integer
x = int(input("enter the number : "))
f=  1
if(x<0):
    print("factorial cant be found")
elif(x==0):
    print("factorial of x is 1")
else:
    for i in range(1,x+1):
        f = f*i
    print(f)