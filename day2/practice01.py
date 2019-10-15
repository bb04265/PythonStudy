num = int(input("어디까지 계산할까요 : "))
sum = 0
for x in range(num+1) :
    sum += x
print("1부터 10까지의 정수의 합 = %d" % sum)