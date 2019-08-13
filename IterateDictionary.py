#Python program to iterate over dictionaries using for loops
thisDict={"brand":"Ford","Model":"Mustang","year":1964}
print(thisDict)
#printing only values
for x in thisDict:
    print(thisDict[x])
for x,y in thisDict.items():
    print(x,":",y)
