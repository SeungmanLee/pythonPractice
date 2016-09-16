
# 1.
print("")
print("# 1.")

f = open("number.txt", "wt")
for i in range(1, 11):
    f.write(str(i))
    f.write("\n")

f.close()

f = open("number.txt", "rt")
lines = f.readlines()
for line in lines:
    print(line, end='')

# 2.
print("")
print("# 2.")

'''
사용자로부터 경로를 입력 받은 후 해당 경로에 있는 디렉터리와 파일 목록을 flist.txt라는 파일로 출력하는 함수를 작성하세요.
'''


import os

def print_listdir(pwd):
    listdirs = os.listdir(pwd)
    f = open("first.txt", "wt")

    for line in listdirs:
        f.write(line)
        f.write("\n")

    f.close()


print_listdir("/home/smlee/PycharmProjects")