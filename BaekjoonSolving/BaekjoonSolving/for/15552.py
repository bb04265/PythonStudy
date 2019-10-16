import sys
import timeit
start = timeit.default_timer()
stop = timeit.default_timer()

T = int(input())

for i in range(T) :
    data = sys.stdin.readline().split(" ")
    print(int(data[0])+int(data[1]))
print(stop - start)