
#
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b


# -*- coding: UTF-8 -*-

a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

# 不等于 - 比较两个对象是否不相等。python3 已废弃。
# if a <> b:
#     print
#     "3 - a 不等于 b"

# else:
#     print
#     "3 - a 等于 b"

if a < b:
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")

if a > b:
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")

if b >= a:
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")




# age = int(input("请输入你家狗狗的年龄: "))
# print("")
#
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
#
# ### 退出提示
# input("点击 enter 键退出")


# 程序演示了 == 操作符
# 使用数字
print(5 == 6)
# 使用变量
x = 5
y = 8
print(x == y)


# number = 8
# guess = -1
# print("数字猜谜游戏!")
#
# while guess != number:
#     guess = int(print('请输入猜测的数字:'))
#     if guess == number:
#         print('恭喜你猜对了')
#     elif guess > number:
#         print('你猜的数字大了')
#     elif guess < number:
#         print('你猜的数字小了')



num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")




