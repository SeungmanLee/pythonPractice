#!/usr/bin/python
# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("")
        print("*************************")
        print("name  :", self.name)
        print("email :", self.email)
        print("addr  :", self.addr)
        print("*************************")


def set_contact():
    name = input("이름 :")
    email = input("email :")
    addr = input("주소 :")
    c = Contact(name, email, addr)
    return c


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()


def delete_contact(contact_list):
    name = input("input delete name:")
    for i, contact in enumerate(contact_list):
        if name == contact.name:
            del contact_list[i]


def store_contact(contact_list):
    f = open("contact_db.txt", 'wt')
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.email + '\n')
        f.write(contact.addr + '\n')
    f.close()


def load_contact_list(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 3
    num = int(num)

    for i in range(num):
        name  = lines[i * 3].rstrip('\n')
        email = lines[i * 3 + 1].rstrip('\n')
        addr  = lines[i * 3 + 2].rstrip('\n')
        c = Contact(name, email, addr)
        contact_list.append(c)
    f.close()


def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("입력 :")

    return int(menu)


def main():
    contact_list = []
    load_contact_list(contact_list)

    while True:
        menu = print_menu()

        if 1 == menu:
            contact = set_contact()
            contact_list.append(contact)
        elif 2 == menu:
            print_contact(contact_list)
        elif 3 == menu:
            delete_contact(contact_list)
        elif 4 == menu:
            store_contact(contact_list)
            break

    # set_contact()



if __name__ == '__main__':
    main()




