#수를 입력받아 그 수가 짝수인지 홀수인지 판별하는 프로그램

while True:
    input_num = int(input("Enter the number : "))
#while 무한루프를 쓰기위해서 True를 쓴다
    if input_num % 2 == 0 and input_num > 0:
        print(input_num, "is even number")
    elif input_num % 2 == 1 and input_num >0:
        print(input_num, "is odd number")

#홀짝을 판별한다
    else :
        print("EXIT")
        break
#모두 다 아니고 0을 입력하면 EXIT을 출력하고  break를 써서 while문에서 나가게한다.