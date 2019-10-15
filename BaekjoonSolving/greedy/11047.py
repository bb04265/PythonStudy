def greedy():
    coin = []
    N, K = list(map(int, input().split(' ')))
    for i in range(N) :
        coin.append(int(input()))
    coin.sort(reverse=True)

    cnt = 0
    for i in coin:
        cnt += K // i
        K = K % i
    print(cnt)
greedy()