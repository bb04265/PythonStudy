class PhoneBook:
    def __init__(self, name, number):
        self.name = name
        self.number = number

def save_contact():
    contacts = {}
    print("이름과 전화번호를 입력하세요")
    name = input("이름 : ")
    number = input("전화 : ")
    contact = PhoneBook(name, number)
    contacts[contact.name] = contact.number
    if name == 'q':
        find_contact(contacts)
    return contacts

def find_contact(contacts):
    print("전화번호 검색합니다")
    while True:
        name = input("이름을 입력하세요 : ")
        if name in contacts:
            return contacts[name]


while True:
    save_contact()