#Python program to create a tuple with numbers and print one item
values=input("Enter the values separated by comma:")
tuple1=tuple(values.split(","))
tuple1=tuple(tuple1)
print(tuple1)
print(tuple1[0])
print(tuple1[-1])
