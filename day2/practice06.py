import random

input_num = int()
rand_num = random.randint(1,int(input("범위 : ")))
try_num = 0

while input_num != rand_num:
    input_num = int(input("정답 : "))
    if input_num > rand_num:
        print("입력 값이 크다")
        try_num += 1
    elif input_num < rand_num:
        print("입력 값이 작다")
        try_num += 1
    else:
        try_num += 1
print(try_num)