num=int(input("enter total how many numbers: "))
arr=[]
sum=0
for i in range(num):
    n=int(input("enter values: "))
    arr.append(n)

for j in arr:
    sum+=j

print("sum of all elements: ",sum)