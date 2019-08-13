#Python program to check whether a specified value is contained in a group of values
values=input("Enter the group of values separated by comma:")
list1=values.split(",")
key=input("Enter the specified values to check whether present in the group of values:")
if list1.count(key):
    print("True")
else:
    print("False")
