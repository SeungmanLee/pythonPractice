
# 1.
print("# 1")
for i in range(1, 5):
    print(end="*")


# 2.
print("")
print("# 2")

for i in range(1, 5):
    for j in range(1, 5):
        print(end="*")
    print("")

# 3.
print("")
print("# 3")

for i in range(1, 6):
    for j in range(0, i):
        print(end="*")
    print("")


# 4.
print("")
print("# 4")

for i in range(1, 6):
    j = 6 - i
    while j > 0:
        print(end="*")
        j -= 1
    print("")


# 5.
print("")
print("# 5")

for i in range(1, 6):
    for j in range(1,6):
        k = j + i
        if k <= 5:
            print(end=" ")
        else:
            print(end="*")
    print("")


# 6.
print("")
print("# 6")

for i in range(1, 6):
    for j in range(1,6):
        if i > j:
            print(end=" ")
        else:
            print(end="*")
    print("")


# 7.
print("")
print("# 7")

'''
    *
   ***
  *****
 *******
*********
'''

mid = 10 / 2
for i in range(1, 6):
    for j in range(1, 10):
        if j == mid:
            print(end="*")
        elif j < mid:
            k = i + j
            if k <= mid:
                print(end=" ")
            else:
                print(end="*")
        else:
            k = j - mid
            if i > k:
                print(end="*")
    print("")


# 8.
print("")
print("# 8")

mid = 10 / 2
for i in range(1, 6):
    for j in range(1, 10):
        if j == mid:
            print(end="*")
        elif j < mid:
            if i > j:
                print(end=" ")
            else:
                print(end="*")
        else:
            k = j - mid
            if i <= k:
                print(end="*")
    print("")


# 9.
print("")
print("# 9")

apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for apt in apart:
    for a in list(apt):
        if a in arrears:
            print("skip %s" % a)
        else:
            print("delivery %s" % a)

