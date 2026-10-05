r=int(input("enter num of row: ")) 
for i in range(r):
    print("  "*(r-i+1),end=" ")
    for j in range(2*i+1):
        print(chr(65+j),end=" ")
    print()
    