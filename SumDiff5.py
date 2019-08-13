#Python program that will return true if the two given integer values are equal or their sum or difference is 5
def SumDiff5(a,b):
    if a==b:
        return True
    elif a+b==5:
        return True
    elif a-b==5:
        return True
    elif b-a==5:
        return True
    else:
        return False

x=int(input("Enter the first Number: "))
y=int(input("Enter the second Number: "))
print(SumDiff5(x,y))
