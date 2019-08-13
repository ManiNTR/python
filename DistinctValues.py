#Python function that takes a sequence of numbers and determines if all the numbers are different from each other
values=input("Enter the sequence of Numbers separated by comma: ")
list1=values.split(",")
l=[]
for i in list1:
    if list1.count(i):
        l.append(i)
print(set(l))
