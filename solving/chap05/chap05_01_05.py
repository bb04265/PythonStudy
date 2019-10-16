def is_prime():
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True

num = int(input())
print(is_prime())