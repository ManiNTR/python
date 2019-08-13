#Python program to get the key, value and item in a dictionary
thisDict={"brand":"Ford","Model":"Mustang","year":1964}
print("The Dictionary values are: ",thisDict)
print("Key  :  values")
for i,j in thisDict.items():
    print(i,":",j)
print("Key")
for i in thisDict:
    print(i)
print("Values")
print(thisDict.get("brand"))
print(thisDict.get("Model"))
