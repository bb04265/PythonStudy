maxValue = 0
minValue = 0
count = 1
n_list = []


for i in range(5):
    num = int(input("%d번째 숫자 "%count))
    n_list.append(num)
    count += 1

n_list.sort(reverse=True)
print("최대값 : %d"%n_list[0])
print("최소값 : %d"%n_list[-1])
