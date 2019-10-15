def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True

while True:
    print(is_prime(int(input("정수 입력 : "))))
