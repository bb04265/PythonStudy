appleP = 1000
grapeP = 3000
pearP = 2000
manP = 500
total = 0

num = list(map(int, input().split()))
total = (num[0]*appleP)+(num[1]*grapeP)+(num[2]*pearP)+(num[3]*manP)
if num[1] >= 3:
    print(total*0.9)
else:
    print(total)