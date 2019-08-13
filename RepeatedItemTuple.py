#Python program to find the repeated items of a tuple
values=input("Enter the values separated by comma:")
list1=values.split(",")
tuple1=tuple(list1)
l=[]
for i in tuple1:
    if tuple1.count(i)>1:
        l.append(i)
print("The repeated item in tuple are: ")
print(set(l))
        

        
