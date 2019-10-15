num = int(input("어디까지 계산할까요 : "))
sum = 0

if num >= 0:
    for x in range(num):
        sum += num

else :
    for x in range(num,0):
        sum += num

print("0부터", num, "까지의 정수의 합 =", sum)