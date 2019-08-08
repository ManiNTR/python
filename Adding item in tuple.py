values=input("Enter the values separated by comma:")
tuple1=tuple(values.split(","))
print("The elements in the tuple are:",tuple1)
key=input("Enter the item to be added to tuple:")
list1=key.split(",")
list2=list(tuple1)
list2.extend(list1)
print("The tuple elements are: ",tuple(list2))

