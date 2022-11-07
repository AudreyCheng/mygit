

list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

# 删除列表中的元素
del list[0]
print(list)

# Python列表脚本操作符
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
#
# 如下所示：
# Python        表达式	 结果	描述
# len([1, 2, 3])	3	长度
# [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
# ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
# 3 in [1, 2, 3]	True	元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代

list1 = [1, 2, '3', 'a', 100, 'aaaa']
print(list1)

print(len(list1))        # 长度为 6

print(list+list1)        # 字符串拼接

print(list1 * 3)         # 字符元素复制

if 2 in list1:           # 元素是否在列表中
    print('3在list1')
else:
    print('3不在list1')

for x in [1, 2, 3]: print(x, end=" ")      # 列表中的元素迭代






