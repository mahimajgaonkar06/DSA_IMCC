num=int(input("enter total how many numbers: "))
arr=[]
counteve=0
countodd=0

for i in range(num):
    n=int(input("enter elements: "))
    arr.append(n)
for j in arr:
    if (j%2==0):
        counteve+=1
    else:
        countodd+=1
print("even nums: ",counteve)
print("odd nums: ",countodd)