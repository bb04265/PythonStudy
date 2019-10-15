#0을 입력하면 입력은 종료가 되고 앞서 입력한 숫자들을 더하여 출력하는 프로그램

sum = 0
#총 합을 담아 줄 변수를 만든다
while True:
#while문을 사용해서 숫자를 계속 입력받을 수 있다
    input_num = int(input("숫자를 입력하세요: "))
    sum += input_num

    if input_num == 0:
        break
#만약에 0을 입력하면 while문을 빠져나갈수 있게 한다
print("총 합은 :", sum, "입니다.")