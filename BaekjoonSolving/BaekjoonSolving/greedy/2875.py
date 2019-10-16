N, M, K = map(int, input().split(' '))
team = 0

while True:
    N = N - 2
    M = M - 1
    if N < 0 and M < 0 and N + M > K:
    team += 1
else :
    break
print(team)