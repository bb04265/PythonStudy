num = input()
total = 0

for i in range(len(num)):
    total += int(num[i])

if total % 3 == 0 :
    print(num)
else :
    print('-1')