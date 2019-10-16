star = int(input())

if star < 1 or star > 100 :
    raise ValueError("error!")

for i in range(1, star+1):
    print(" "*(star-i)+"*"*i)