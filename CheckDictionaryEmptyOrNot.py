#Python program to check a dictionary is empty or not
num={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6}
print(num)
if not num.items():
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")
dictionary={}
print(dictionary)
if not dictionary.items():
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")
