num = int(input())

if num > 100000 :
    raise ValueError("error")

for i in range(num):
    print(i+1)