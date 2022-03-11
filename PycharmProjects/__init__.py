var1 = 10
while var1 > 0:
    print('当期变量值为 :', var1)
    var1 = var1 - 1
    if var1 == 5:
        break
print("Good bye!")

var2 = 10
while var2 > 0:
    var2 = var2 - 1
    if var2 == 5:
        continue
    print('当前变量值 :', var2)
print("Good bye!")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        print(n, '\t是质数')

# else子句在穷尽列表(for循环)或条件变为false(while循环)导致循环终止时被执行,但循环被break终止时不执行。
print("\n\n")


# f = open("/Users/swqt/Desktop/peace.txt", "r+")
# str1 = f.read()
# print(str1)
#
# f = open("/Users/swqt/Desktop/peace.txt", "w")
# f.write("写入，会覆盖之前的内容 ")
#
# f = open("/Users/swqt/Desktop/peace.txt", "r")
# str1 = f.read()
# print(str1)
#
# f = open("/Users/swqt/Desktop/peace.txt", "a+")
# f.write("追加，在之前内容的后面添加\n")
#
# f = open("/Users/swqt/Desktop/peace.txt", "r")
# str1 = f.read()
# print(str1)
# f.close()
#
# with open("/Users/swqt/Desktop/peace.txt", "w") as f:
#     for i in range(5):
#         f.write("彭博")
#         f.write("\n")
# with open("/Users/swqt/Desktop/peace.txt", "r") as f:
#     peace = f.read()
# print(peace)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        print(self.a)
        print(self.b)
        print(other.a)
        print(other.b)
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

print('****************************************************************************')

import re

str1 = 'who so What and where when you 12345'
t1 = re.findall(r'\bw[a-z]*|\d+', str1, flags=re.I)
t2 = re.search('and', str1).span()
print(t1)
print(t2)
str2 = "Cats are smarter than dogs"
t3 = re.match(r'(.*) are (.*?) (.+)', str2, re.M | re.I)
t4 = re.sub(r'\d+', '6789', str1)
print(t3.group(1, 2, 3))
print(t4)
str3 = 'pe6a7ce6gai6ve777'
t5 = re.compile(r'\d+')
t6 = t5.findall(str3, 1, 8)
print("t6:", t6)


print()
print()
# import random

# i = 1
# a = random.randint(0, 100)
# b = int(input('请输入0-100中的一个数字\n然后查看是否与电脑一样：'))
# while a != b:
#     if a > b:
#         print('你第%d输入的数字小于电脑随机数字' % i)
#         b = int(input('请再次输入数字:'))
#     else:
#         print('你第%d输入的数字大于电脑随机数字' % i)
#         b = int(input('请再次输入数字:'))
#     i += 1
# else:
#     print('恭喜你，你第%d次输入的数字与电脑的随机数字%d一样' % (i, b))


print("\n")
# f1 = 0
# f2 = 1
# num = int(input("输入你需要的项数："))
# while num < 1:
#     if num <= 0:
#         print("请输入正整数！！")
#         num = int(input("再次输入你需要的项数："))
#         continue
#     break
# if num == 1:
#     print("斐波拉契数列:%d" % f1)
#     # print("斐波拉契数列:{}".format(f1))
# else:
#     print("斐波拉契数列:")
#     print(f1, f2, end=" ")
#     for n in range(1, num - 1):
#         f = f1 + f2
#         f1, f2 = f2, f1 + f2
#         print(f, end=" ")

# people = list(range(1,31))
# while len(people) > 15:
#     i = 1
#     while i < 9:
#         people.append(people.pop(0))
#         i += 1
#     print('{}号下船了'.format(people.pop(0)))



sum = 0
a = input().split()
for i in range(len(a)):
    sum = sum + int(a[i])
print(sum)