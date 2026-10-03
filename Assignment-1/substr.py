main=input("enter main string: ")
substr=input("enter substring to be found: ")
count = 0

for i in range(len(main) - len(substr) + 1):
    if main[i:i+len(substr)] == substr:
        print("Substring found at index:", i)
        count += 1

print("Total occurrences:", count)