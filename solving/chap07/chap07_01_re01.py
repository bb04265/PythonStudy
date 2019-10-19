n_list = []

for i in range(1, 101):
    if i%3==0 and i%5==0:
        n_list.append(i)

print("3과 5의 공배수 : ", n_list)
print("개수는 : ", len(n_list))