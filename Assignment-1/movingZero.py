n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

result = []

# First add all non-zero elements
for i in arr:
    if i != 0:
        result.append(i)

# Then add zeros
for i in arr:
    if i == 0:
        result.append(i)

print("Rearranged array:", result)