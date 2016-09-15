
# https://wikidocs.net/2843
# python practice
# 2016-09-14

# 1.

daum = 89000

naver = 751000

count_daum = 100

count_naver = 20

current_total_money = ((daum * count_daum) + (naver * count_naver))

print(current_total_money)

# 2.

daum_down = daum - (daum * 0.05)

naver_down = naver - (naver * 0.1)

downed_current_total_money = ((daum_down * count_daum) + (naver_down * count_naver))

print(downed_current_total_money)

print(current_total_money - downed_current_total_money)

# 3. C = (F-32) / 1.8

f = 50
c = (f - 32) / 1.8

print("Celcious : ", c)

# 4.

print("pizza\n" * 10)
'''
i = 0
for i ; i < 10 ; i++ :
    print("pizza")

'''


# 5.

naver = 1000000
print("naver price start : ", naver)

# 월요일 종가
naver *= 0.7

# 화요일 종가
naver *= 0.7

# 수요일 종가
naver *= 0.7

print("수요일 naver price : ", naver)

# 6. pass


# 7.

s = "Daum Kakao"
arr = s.split(' ')

ret = arr[1] + ' ' + arr[0]
print(ret)


# 8.

a = "hello world"

a = a.replace("hello", "hi")

print(a)


# 9.

x = 'abcdef'    # bcdefa

y = x[1:] + x[0]

print(y)





