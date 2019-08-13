#Python program to remove a key from a dictionary
num={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6}
print(num)
num.popitem()
num.pop("one")
print(num)
