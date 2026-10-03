s = input("Enter a sentence: ")

words = s.split()

longest = words[0]
shortest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

    if len(i) < len(shortest):
        shortest = i

print("Longest word:", longest)
print("Shortest word:", shortest)