s_list = list()
while(True):
    names = input("강아지의 이름을 입력하시오 : ")
    if names == "" :
        break

    s_list.append(names)
print("강아지들의 이름 : ", s_list)