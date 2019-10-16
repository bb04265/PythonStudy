while True:
    num = int(input())
    if num % 2 == 0 and num != 0:
        print("%d 는 짝수"%num)
    elif num % 2 == 1 and num != 0:
        print("%d는 홀수"%num)
    else :
        print("EXIT")
        break