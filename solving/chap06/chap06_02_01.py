i = 0
words = []
while i < 5:
    words.append(input())
    i += 1

print(words[2] + words[1] + words[-1])
print(words[2] + words[3] + words[0])
