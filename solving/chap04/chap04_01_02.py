num = int(input())
sum = 0

if num > 0:
    for i in range(num+1):
        sum += i
elif num < 0:
    for i in range(num,0):
        sum += i
else :
    sum = 0

print(sum)