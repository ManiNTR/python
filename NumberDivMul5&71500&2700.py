#Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
l=[]
for i in range(1500,2701):
    if i%5==0:
        l.append(i)
    if i%7==0:
        l.append(i)

print(set(l))
