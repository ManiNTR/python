#Python program to concatenate following dictionaries to create a new one
thisDict={"brand":"Ford","Model":"Mustang","year":1964}
print(thisDict)
feature={"color":"White","Symbol":"Horse"}
print(feature)
this={}
for i in (thisDict,feature):
    this.update(i)
print(this)
