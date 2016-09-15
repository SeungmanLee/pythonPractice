
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

for i in range(1, 6):
    for j in range(1, 10):
        k = i + j
        l = i + j
        if k <= 5:
            print(end=" ")
        elif
        else:
            print(end="*")

#        if l > 6:
#            print(end=" ")
#        else:
#            print(end="*")
    print("")

