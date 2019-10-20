english_dict = {'one':'하나', 'two':'둘', 'three':'셋'}

while True:
    key = input("단어를 입력하시오 : ")
    if key == "exit":
        break

    if key in english_dict:
        print(english_dict[key])
    else:
        print("없음")