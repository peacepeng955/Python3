python = "  pengBo  "
print(python)
print(python.strip())
print(python.title())
print(python.upper())
print(python.lower())
print('\n')

list1 = [ 1, 2, 3, 4, 5]
print(list1[2])
list1.append(6)
print(list1)
list1.remove(2)
print(list1)
list1.reverse()
print(list1)


list2 = ["Python", 12, [1, 2, 3], 3.14, True]
print(list2)
list2[1] = 17
print(list2)
print('\n')


setpram = {0, 1, 2, 3, 4, 5, 5, 4, 3}
print(setpram)
print('\n')


print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
print(dict(Runoob=1, Google=2, Taobao=3))
print({x: x ** 2 for x in (2, 4, 6)})
dict = {'name': 'peace', 'age': '23'}
print(dict)
dict['sex'] = 'male'
print(dict)
print(dict.keys())  # 输出所有键
print(dict.values())  # 输出所有值
print(dict['name'])
del dict['age']
print(dict)
print('\n')


if list1[0] == 'peace':
    print('123456')
else:
    print('FFF')

if dict['name'] == 'peace':
    print('666')
else:
    print('GG')

for i in list2:
    print(i)

sum = 0
for i in range(1, 10, 1):
    sum += i
print(sum)

print('\n')


def temp(x):
    y = x ** 2 + 2 * x
    return y


Va = temp(2)
print(Va)

str = "pengbo "
print(str[0:2])
print(str[0:-1])
print(str * 2 + ' nihao')

# 键盘输入# 键盘输入# 键盘输入# 键盘输入# 键盘输入# 键盘输入

# pboom = input('')
# print(type(pboom))
# print(pboom * 2 + 'nihao')

# 键盘输入# 键盘输入# 键盘输入# 键盘输入# 键盘输入# 键盘输入


x = "a"
y = "b"
print(x)
print(y)
print('---------')
# 不换行输出  #不换行输出  #不换行输出
print(x, end=" ")
print(y, end=" ")
print('\n')
print('\n')
print('\n')


# 翻转字符串
# 假设列表 list = [1,2,3,4],
# list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
# inputWords[-1::-1] 有三个参数
# 第一个参数 -1 表示最后一个元素
# 第二个参数为空，表示移动到列表末尾
# 第三个参数为步长，-1 表示逆向
def words(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]

    output = ' '.join(inputWords)
    # 重新组合字符串
    return output


if __name__ == "__main__":
    input = 'I want to swim with you'
    rw = words(input)
    print(rw)
    print('\n')
    print('\n')

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
# set可以进行集合运算

set1 = set('abracadabra')
set2 = set('alacazam')
print(set1)
print(set2)
print(set1 - set2)  # a 和 b 的差集
print(set1 | set2)  # a 和 b 的并集
print(set1 & set2)  # a 和 b 的交集
print(set1 ^ set2)  # a 和 b 中不同时存在的元素


# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo1(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ",arg1)
    print(vartuple)


printinfo1(70, 60, 50)


# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo2(arg2, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg2)
    print(vardict)


printinfo2(1, a=2, b=3)



