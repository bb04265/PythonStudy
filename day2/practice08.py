input_num = int(input("정수를 입력하시오 : "))
sum = 0

for x in range(input_num+1):
    if x % 3 == 0 :
        sum += x

print("1부터 ",input_num,"까지의 3의 배수의 합은", sum, "입니다.")