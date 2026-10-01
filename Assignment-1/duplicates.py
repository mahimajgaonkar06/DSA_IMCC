num=int(input("enter total nums: "))
new=[]
org=[]

for i in range(num):
    n=int(input("enter val: "))
    org.append(n)

for j in org:
    if j not in new:
        new.append(j)

print("non duplicated array: ",new)
    