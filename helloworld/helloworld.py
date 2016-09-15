
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



