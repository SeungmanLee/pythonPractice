
# 1.
print("")
print("# 1.")

def mysum(x, y):
    return (x + y) / 2

print(mysum(2, 4))

# 2.
print("")
print("# 2.")

def get_max_min(data_list):
    mx = max(data_list)
    mn = min(data_list)
    return (mx, mn)

print(get_max_min([1, 2, 3, 4, 5, 6]))

# 3.
print("")
print("# 3.")

def get_txt_list(path, extention="py"):
    import os
    fileLIst = os.listdir(path)
    txt_list = []
    for i in fileLIst:
        if i.endswith(extention):
            txt_list.append(i)

    return txt_list

print(get_txt_list("E:\PycharmProjects\pythonPractice\helloworld", extention="3.py"))


# 4.
print("")
print("# 4.")

def get_bmi(weight, height):
    height = height * 0.01
    bmi = weight / (height * height)
    '''
    BMI <18.5, 마른체형
    18.5 <= BMI < 25.0, 표준
    25.0 <= BMI < 30.0, 비만
    BMI >= 30.0, 고도 비만
    '''
    if bmi < 18.5:
        return "마른체형"
    elif 18.5 <= bmi < 25.0:
        return "표준"
    elif 25.0 <= bmi < 30.0:
        return "비만"
    else:
        return "고도비만"

print(get_bmi(60, 180))
print(get_bmi(70, 180))
print(get_bmi(90, 180))
print(get_bmi(100, 180))


# 5.
print("")
print("# 5.")

'''
while True:
    w = input("무게:")
    h = input("키:")

    ret = get_bmi(float(w), float(h))
    print(ret)
'''


# 6.
print("")
print("# 6.")

def get_triangle_area(width, height):
    return width * height / 2

print(get_triangle_area(3, 5))



# 7.
print("")
print("# 7.")

def mysum2(start, end):
    sum = 0
    for i in range(start, end):
        sum += i
    return sum

print(mysum2(1, 5))


def mysum3(start, end):
    return sum(range(start, end+1))


# 8.
print("")
print("# 8.")

def print_3words(word_list):
    ret = []
    for i in word_list:
        ret.append(i[:3])
    return ret

print(print_3words(['Seoul', 'Daegu', 'Kwangju', 'Jeju', 'gi']))






