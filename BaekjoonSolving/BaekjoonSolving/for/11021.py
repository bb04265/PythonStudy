num = int(input())

for i in range(num):
    A, B = list(map(int, input().split(" ")))
    if A > 10 or B > 10 :
        raise ValueError("error!")

    print("Case #%s: %s"%(i+1, A+B))