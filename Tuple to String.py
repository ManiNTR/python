values=input("Enter the values separated by comma:")
tuple1=tuple(values.split(","))
result=""
for i in tuple1:
    result=result+i
print(result)
