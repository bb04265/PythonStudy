list1 = list()
for i in range(1,101) :
    if i % 3 == 0 and i % 5 == 0:
        list1.append(i)
print("3과 5의 공배수는 : ", list1)
print("개수는 : ", len(list1))