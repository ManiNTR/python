values=input("Enter the values separated by comma:")
tuple1=tuple(values.split(","))
print("The elements in the tuple are:",tuple1)
key=input("Enter the items to be removed from the tuple:")
list1=key.split(",")
list2=list(tuple1)
for i in list1:
    list2.remove(i)
print("The elements of the tuple are: ",tuple(list2))
