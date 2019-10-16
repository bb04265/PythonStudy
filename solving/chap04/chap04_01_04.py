F=0

for i in range(0,101,10):
    C = (F - 32) * (5 / 9)
    print("%d -> %f"%(F,round(C)))
    F += 10