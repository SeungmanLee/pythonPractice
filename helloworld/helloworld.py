
print("hello world")


mystring = "this is hello world "
print(mystring)

print(mystring.capitalize())

print(mystring.upper())


length = len(mystring)

print(length)


print(mystring[0:5])

print(mystring[5:150])

splited = mystring.split(' ')


print(splited)


print(type(splited))

print(type(3.14150))


'''
if list.__class__ == type(splited):
    print("haha")
else
    print("asdfggg")
'''


interest = ["s전자", "lg전자", "never"]

print(interest[0])
print(interest[1])
print(interest[2])


mystock = ['Naver', 5000]

print(mystock)

mystock = []

print(mystock)

buy_list = ['naver', 5000]
print(buy_list[0])
print(buy_list[1])


print(interest[-1])
print(interest[-2])
print(interest[-3])



print(interest)
interest.append("newnewnew")
print(interest)
interest.remove("never")
print(interest)

interest.pop(1)
print(interest)

interest.insert(1, "LG전자")
print(interest)


print(len(interest))


print(interest[-1])

del interest[-1]
print(interest)

del interest[0]
print(interest)

del interest[0]
print(interest)


t = ("SS", "LG", "SK")
print(t)


l = len(t)
print(l)

print(t[0])
print(t[-1])


# t[0] = "aa"    error

print(t[0:2])


curr_price = {}

print(type(curr_price))
print(curr_price)

curr_price["aa"] = "good"
curr_price["아주"] = "nice"
curr_price["hello"] = "world"

print(curr_price)


print(len(curr_price))

print(curr_price["aa"])

# error print(curr_price[0])

print(curr_price.keys())
print(curr_price.values())

del curr_price['aa']
print(curr_price)

ty = curr_price.keys()

print(type(ty), ty)

print(type(list(ty)))


print("hello" in curr_price)
print(type("hello111" in curr_price))

print(curr_price["아주"])


# if

wikibooks_cur_price = 11000

if wikibooks_cur_price <= 50000:
    print("Buy 5")
    print("Buy 6")
else:
    print("Not buy")


price = 2100

if price < 1000:
    bid = 1
elif 1000 <= price < 2000:
    bid = 2
elif 2000 <= price < 3000:
    bid = 2.5
else:
    bid = 3

print("bid : ", bid)


# for

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("for : ", i)


print(list(range(1, 10)))


for i in range(1, 10):
    print("range : ", i)


stocks = ["aa", "bb", "cc"]
for company in stocks:
    print("%s is ok " % company, "zzz %d" % 99)


stocks = {"aa": 11, "bb": 22, "cc": 33}

for k, v in stocks.items():
    print("key is %s, value is %s" % (k, v))


for k in stocks.keys():
    print("key %s , value is %s" % (k, stocks[k]))


# for

wikibooks = 30000
cnt = 0

while cnt < 5:
    cnt += 1
    wikibooks += wikibooks * 0.3

print("price is %s" % wikibooks)


num = 0
while num <= 10:
    num += 1
    if num % 2 == 0:
        print("even %s" % num)
    else:
        print("odd %s" % num)


