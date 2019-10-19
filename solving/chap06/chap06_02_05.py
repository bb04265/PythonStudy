count = 1
n_list = []
for i in range(5):
    nums = int(input("%d번째 숫자 : "%count))
    n_list.append(nums)
    count += 1

print(n_list[::-1])