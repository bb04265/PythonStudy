num = int(input())
total = 0

for i in range(1,num+1):
    if i%3 == 0:
        total += i
print("1부터 %d사이의 모든 3의 배수의 합은 %d입니다"%(num, total))
