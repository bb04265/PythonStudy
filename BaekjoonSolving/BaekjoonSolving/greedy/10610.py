
while True :
    num = input()
    if num == 'exit':
        break
    total = 0
    for i in range(len(num)):
        total += int(num[i])
        new_num = int("".join(sorted(num, reverse=True)))

    if total % 3 == 0 and ('0' in str(new_num)):
        print(new_num)

    else :
        print('-1')
