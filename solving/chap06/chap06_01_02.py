dogs_list = []

while True:
    dogs = input("강아지의 이름을 입력하시오 : ")
    if dogs == "":
        break
    dogs_list.append(dogs)

print("강아지들의 이름:")
print(dogs_list)
print("총 %d 마리입니다"%len(dogs_list))
