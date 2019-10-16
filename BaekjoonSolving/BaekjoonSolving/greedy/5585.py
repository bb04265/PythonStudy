def greedy():
    coin = [500, 100, 50, 10, 5, 1]
    money = 1000-(int(input()))
    cnt = 0
    for i in coin:

        cnt += money // i
        money = money % i

    print(cnt)
greedy()