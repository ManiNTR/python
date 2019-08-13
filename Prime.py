#Program to check the prime number
num=int(input("Enter the number:"))
prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
if(prime==True):
    print("The given number is prime")
else:
    print("The given number is not a prime")
