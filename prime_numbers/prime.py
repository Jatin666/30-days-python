print("Enter the number to check whether it is prime or not")
a = int(input("Enter the number: "))
for i in range(2,a):
    if (a%i==0):
        print("its not prime number")
        break
    else:
        print("its an prime number")
        break