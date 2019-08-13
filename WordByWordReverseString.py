#Python program to reverse a string word by word
string=input("Enter the String")
list1=string.split(" ")
print("The given string is ",string)
rev_str=list1[::-1]
result=""
for i in rev_str:
    result=result+i+" "
print("The reverse string is ",result)

