num=[10,2,30,21,50,36]
min=num[0]
max=num[0]
for i in num:
    if(i<min):
        min=i

    if(i>max):
        max=i
print("min",min)
print("max",max)
print("second min",smin)
print("second max",smax)
