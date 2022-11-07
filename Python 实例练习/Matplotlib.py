

# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 定义变量 x y z
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1

# 定义图片大小
plt.figure(figsize = (8,4))

# 作图、设置线条颜色、大小
plt.plot(x,y,label = '$\sinx+1$', color = 'red', linewidth = 2 )
# 作图、设置线条颜色、大小
plt.plot(x,z,'--b',label = '$\cosx^2 + 1$', linewidth = 1  )
# 设置坐标轴
plt.xlabel('Time(s)')
plt.ylabel('Volt')
# 设置标题
plt.title('A Simple Example')
# 设置竖坐标的范围
plt.ylim(0,2.2)
# 显示图例
plt.legend()
# 显示作图结果
plt.show()