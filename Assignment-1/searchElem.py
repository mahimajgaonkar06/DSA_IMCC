num=int(input("enter total how many numbers: "))
arr=[]

for i in range(num):
    n=int(input("enter numbers: "))
    arr.append(n)

srch=int(input("enter a no. to find: "))
if srch in arr:
    print("number present")
    print("position: ",arr.index(srch))
else:
    print("number not present")
