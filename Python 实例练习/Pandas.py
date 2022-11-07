
# -*- coding: utf-8 -*-

import pandas as pd
s = pd.Series([1,2,3], index = ['a','b','c'])                 # 创建一个序列 s
d = pd.DataFrame([[1,2,3],[4,5,6]], columns = ['a','b','c'])  # 创建一个表 d
d2 = pd.DataFrame(s)   # 也可以用已有的序列创建表格


d.head()        # 预览前5行
d.describe()    # 数据基本统计量


print(d.head())
print(d.describe())


# pd.read_excel('data.xls')
# pd.read_csv('data.csv', encoding='utf-8')
