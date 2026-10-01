num=int(input("enter total how many numbers: "))
arr=[]
min=0
max=0
for i in range(num):
    n=int(input("Enter values: "))
    arr.append(n)

arr.sort()

print("smallest val: ",arr[0])
print("second smallest val: ",arr[1])
print("largest val: ",arr[-1])
print("second largest val: ",arr[-2])

