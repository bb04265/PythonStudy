H, M = list(map(int, input().split(" ")))
if H == 0:
    H = 24
if M > 45 :
    print(H ,":",M-45)
else :
    print(H-1, ":", (60+M)-45)