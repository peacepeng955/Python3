age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

num = 0
while num < 20:
    num = int(input("输入一个数字："))
    if num % 2 == 0:
        if num % 3 == 0:
            print("你输入的数字可以整除 2 和 3")
        else:
            print("你输入的数字可以整除 2，但不能整除 3")
    else:
        if num % 3 == 0:
            print("你输入的数字可以整除 3，但不能整除 2")
        else:
            print("你输入的数字不能整除 2 和 3")

n = int(input("输入n的值："))
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))
