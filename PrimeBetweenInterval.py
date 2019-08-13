#Program to print all the prime numbers in an interval
start_value=int(input("Enter the starting interval: "))
end_value=int(input("Enter the ending interval :"))
num=[]
for i in range(start_value,end_value+1):
    num.append(i)
print(num)
prime=[]
for i in range(2,end_value+1):
    for j in num:
        if j%i==0:
            continue
        else:
            prime.append(j)
print(set(prime))
