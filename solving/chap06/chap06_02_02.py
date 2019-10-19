count = 1
total = 0
n_list = []

for i in range(3):
    nums = int(input("%d번째 숫자 : "%count))
    n_list.append(nums)
    count += 1

for n in range(len(n_list)):
    total += n_list[n]

print("합계 : ", total)