

'''
file
https://wikidocs.net/2578

'''

import os

pwd = os.getcwd()
print(pwd)
f = open(pwd + "/samplelist.txt", "rt")

print(f)

lines = f.readlines()
for line in lines:
    print(line, end='')


fw = open("samplewrites.txt", "wt")
fw.write("test\n")
fw.write("한글이다\n")
fw.close()

