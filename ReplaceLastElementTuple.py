#Python program to replace last value of tuples in a list.
tuple1=(1,2,3,4,5,6,7,8,9)
print(tuple1)
list1=list(tuple1)
list1[-1]=list1[-1]+10
print(tuple(list1))
