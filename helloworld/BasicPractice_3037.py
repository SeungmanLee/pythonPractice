
'''
09/11	488,500
09/10	500,500
09/09	501,000
09/08	461,500
09/07	474,500
'''

# 1.

naver_end_price = []
print(type(naver_end_price))

naver_end_price.append(474500)
naver_end_price.append(461500)
naver_end_price.append(501000)
naver_end_price.append(500500)
naver_end_price.append(488500)
print(naver_end_price)


# 2.
print(max(10, 2))

m = max(naver_end_price[0], naver_end_price[1])
m = max(naver_end_price[2], m)
m = max(naver_end_price[3], m)
m = max(naver_end_price[4], m)

mx = m

print(mx)

print("헐 : ", max(naver_end_price))

# 3.
m = min(naver_end_price[0], naver_end_price[1])
m = min(naver_end_price[2], m)
m = min(naver_end_price[3], m)
m = min(naver_end_price[4], m)

mn = m
print(mn)

print("헐 : ", min(naver_end_price))


# 4.

print(mx - mn)

# 5.

print(naver_end_price[2])



# 6.

naver_end_price2 = {}

naver_end_price2['09/11'] = 488500
naver_end_price2['09/10'] = 500500
naver_end_price2['09/09'] = 501000
naver_end_price2['09/08'] = 461500
naver_end_price2['09/07'] = 474500

print(naver_end_price2)

# 7.
print(naver_end_price2["09/09"])
