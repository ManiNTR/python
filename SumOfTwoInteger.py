#Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
def SumOFTwoInteger(a,b):
    s=a+b
    if s in range(15,20):
        return 20
    else:
        return s
x=int(input("Enter the first Number:"))
y=int(input("Enter the second Number:"))
print(SumOFTwoInteger(x,y))
