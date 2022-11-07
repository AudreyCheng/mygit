
# 列表推导式
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
names = ['Bob','Tom','alice','Jerry','Wendyy','Smith']
new_names  = [name.upper() for name in names if len(name) > 5]
print(new_names)

# 计算 30 以内可以被 3 整除的整数：
number =  [i for i in range(30) if i%3 == 0]
print(number)


# 字典表达式
# { key_expr: value_expr for value in collection if condition }
listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：
dir = {x:x**2 for x in (1,2,3)}
print(dir)


# 集合推导式
# { expression for item in Sequence if conditional }
# 计算数字 8，9,10 的平方数：
new_set = {x**2 for x in (8,9,10)}
print(new_set)


# 判断不是 abc 的字母并输出：
a = {x for x in 'abracadabra' if x not in 'abcd'}
print (a)


# 元组推导式
# (expression for item in Sequence if conditional )
# 生成一个包含数字 1~9 的元组：
a = (x for x in range(1,9))
# a 返回的是生成器对象
# 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a))







