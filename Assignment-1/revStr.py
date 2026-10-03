s=input("enter the string: ")

words=s.split()
words.reverse()
print("Reversed str: ",end="")

for i in words:
    print(i,end=" ")