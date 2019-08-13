#Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against an given amount
amount=int(input("Enter the amount:"))
c1,c2,c3,c4,c5,c6=0,0,0,0,0,0
print("The amount is ",amount)
while(amount>10):
    if amount>=500:
        c1=c1+1
        amount=amount-500
        continue
    elif amount>=200:
        c2=c2+1
        amount=amount-200
        continue
    elif amount>=100:
        c3=c3+1
        amount=amount-100
        continue
    elif amount>=50:
        c4=c4+1
        amount=amount-50
        continue
    elif amount>=20:
        c5=c5+1
        amount=amount-20
        continue
    elif amount>=10:
        c6=c6+1
        amount=amount-10

print("The number of notes in the amount: ")
print("Number of 500 notes :",c1)
print("Number of 200 notes :",c2)
print("Number of 100 notes :",c3)
print("Number of 50 notes :",c4)
print("Number of 20 notes :",c5)
print("Number of 10 notes :",c6)
