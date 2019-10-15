class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
# Contact 클래스를 정의하고 생성자함수를 정의한다 
    
    def print_phone(self):
        print("이름 : ", self.name)
        print("전화 : ", self.phone)
# 그 정보를 출력하는 함수를 정의한다

def set_contact():
    print("이름과 전화번호를 입력해 주세요")
    name = input("이름 : ")
    phone = input("핸드폰번호 : ")
    contact = Contact(name, phone)
    return contact
#변수를 입력받고 그 입력한 변수들을 초기화시킨다

def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone + '\n')
    f.close()
#contact_db라는 메모장에 저장될 수 있게 한다. 

def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readline()
    num = len(lines) / 2
    num = int(num)

    for i in range(num):
        name = lines[2 * i].rstrip('\n')
        phone = lines[2 * i + 1].rstrip('\n')
        contact = Contact(name, phone)
        contact_list.append(contact)
    f.close()

def find_contact(contact_list):
    while 1:
        name = input("이름을 입력하세요 : ")
        for i, contact in enumerate(contact_list):
            if contact.name == name:
                print (contact.phone)
                break
        else:
            print("저장된 이름이 없습니다.")
#열거타입으로 contact_list를 만들어서 입력한 이름과 인덱스를 비교해서 휴대폰번호가 출력될 수 있게 한다


def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        contact = set_contact()
        contact_list.append(contact)
        if contact.name == "q":
            store_contact(contact_list)
            print("전화번호 검색합니다")
            find_contact(contact_list)
# run함수를 만들어서 이름과 주소가 set_contact함수가 실행될때 리스트에 계속 저장되게 하고 while 문으로 q입력전까지 반복되게 한다
if __name__ == "__main__":
    run()


