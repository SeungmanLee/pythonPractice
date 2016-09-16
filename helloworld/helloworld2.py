
print(dir())


# from os import listdir

# print(dir())

l = ["DD", "BB", "AA", "CC"]
print(len(l))

for i, stock in enumerate(l):
    print(i, stock)

print(sorted(l))


print(int("30", base=8))

'''
https://wikidocs.net/3455
class 시작할 차례임.

'''


class BusinessCard:
    def __init__(self, name, email, addr):
        print("초기화")
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):

        print(id(self), "-----------------")
        print("name  : ", self.name)
        print("email : ", self.email)
        print("addr  : ", self.addr)

    def test():
        print("what is this")


card1 = BusinessCard("leeseungman", "kyww1119@gmail.com", "Ilsan")
print(type(card1))


print(card1.name)
print(card1.email)
print(card1.addr)

card1.print_info()

card2 = BusinessCard("name2", "email2", "addr2")

print(card2)
print(card2.name)
print(card2.email)
print(card2.addr)

BusinessCard.test()

print("**********************")
card2.print_info()




BusinessCard.print_info(card2)


print(dir())

print(dict())


class Stock:
    market = "Kospi"

print(dict(Stock.__dict__))

print(Stock.market)


class Parent:
    def can_sing(self):
        print("sing a song")

class Child(Parent):
    def can_dance(self):
        print("Every day I'm shuffling")
    pass

c = Child()
c.can_sing()
c.can_dance()

