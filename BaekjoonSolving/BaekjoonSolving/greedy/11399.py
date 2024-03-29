import sys

def greedy(line):
    total_time = 0
    waiting_time = 0
    line.sort() # 시간 순서대로 정렬해야 합이 최소가 된다
    for time in line:
        waiting_time += time
        total_time += waiting_time
    return total_time

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    line = list(map(int, sys.stdin.readline().strip().split()))
    print(greedy(line))