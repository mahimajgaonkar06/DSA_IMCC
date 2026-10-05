num=0
for i in range(0,5):
    for j in range(0,i+1):
        print(chr(65+num),end=" ")
        num+=1
    print()


# for printing 
# A
# B C
# D E F type pyramid use another variable named num=0 and increment it by 1 after printing