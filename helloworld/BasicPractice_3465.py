

# 1.
print("")
print("# 1.")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

# 2.
print("")
print("# 2.")

p1 = Point(10, 10)
print(p1.get())

p1.move(5, 3)
print(p1.get())

p1.setx(3)
p1.sety(5)
print(p1.get())


# 3.
print("")
print("# 3.")

class Stock:
    market = "kospi"

a = Stock()
b = Stock()

print(id(Stock))
print(id(a))
print(id(b))


# 4.
print("")
print("# 4.")

print("a.market:", a.market)
print("b.market:", b.market)
print("Stock.market:", Stock.market)

a.market = "kosdak"
b.market = "nasdak"

print(a.market)
# kosdak

print(b.market)
# nasdak

print(Stock.market)
# kospi



# 5.
print("")
print("# 5.")

'''
class Stock:
    market = kospi

a = Stock()
a.market == kosdak

b = Stock()
b.market == nasdak

'''
