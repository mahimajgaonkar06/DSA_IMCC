num=int(input("enter num: "))
p=len(str(num))
sum=0
n=num
while(num>0):
    sum+=(num%10)**p
    num//=10
if(n==sum):
    print("Armstrong")
else:
    print("not armstrong")