#Python program to combine two dictionary adding values for common keys
thisDict={"brand":"Ford","Model":"Mustang","year":1964}
print(thisDict)
feature={"color":"White","Symbol":"Horse","year":1964}
print(feature)
thisDict["year"]=1984
feature["year"]=1984
newDict={}
for i in (thisDict,feature):
    newDict.update(i)
print("The combination of two Dictionary is ",newDict)
