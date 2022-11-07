
# Python 提供了 for 循环和 while 循环

# while 循环	在给定的判断条件为 true 时执行循环体，否则退出循环体。
# for 循环	重复执行语句
# 嵌套循环	你可以在while循环体中嵌套for循环
#
# 循环控制语句
# 循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：
#
# 控制语句	描述
# break 语句	在语句块执行过程中终止循环，并且跳出整个循环
# continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
# pass 语句	pass是空语句，是为了保持程序结构的完整性。

count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1

print("Good bye!")

# ------------------ 结果：
# The count is: 0
# The count is: 1
# The count is: 2
# The count is: 3
# The count is: 4
# The count is: 5
# The count is: 6
# The count is: 7
# The count is: 8
# Good bye!


count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

# ------------------ 结果：
# 0  小于 5
# 1  小于 5
# 2  小于 5
# 3  小于 5
# 4  小于 5
# 5  大于或等于 5


# 以下
# for 实例中使用了 break 语句，break 语句用于跳出当前循环体：
#
# 实例

sites = ["Baidu", "Google", "Runoob", "Taobao"]

for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break                   # 语句用于跳出当前循环体：
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


# ------------------ 结果：
# 循环数据 Baidu
# 循环数据 Google
# 菜鸟教程!
# 完成循环!

# range()函数

for i in range(10):
    print(i)


for i in range(4,9):
    print(i)

# 也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):

for i in range(0, 10, 3) :
    print(i)


for i in range(-10, -100, -30) :
    print(i)


# 结合range()和len()函数以遍历一个序列的索引,如下所示:
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])


# while 中使用 break：

# 实例
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')


# ------------------ 结果：
#
# 4
# 3
# 循环结束。


# while 中使用 continue：

# 实例
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')


# ------------------ 结果：
# 4
# 3
# 1
# 0
# 循环结束。


# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
#
# pass 不做任何事情，一般用做占位语句，如下实例


