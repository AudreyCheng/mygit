


# """ 题目一：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""

sum = 0
for i in range(1, 5):                              #  百位数
    for m in range(1, 5):                          #  十位数 m
        for n in range(1, 5):                      #  个位数 n
            if i != m and i != n and m != n:       #  不重复
                print(i*100 + m * 10 + n)
                sum += 1

print(f'一共有{sum}个三位数。')









