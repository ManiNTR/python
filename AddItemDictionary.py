#Python program to sum all the items in a dictionary
num={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6}
print(num)
s=0
for i,j in num.items():
    s=s+j

print("The sum of all value in the dictionary are :",s)
