

# -*- coding: utf-8 -*-
# 求解非线性方程组 2x1 - x2^2 = 1, x1^2 - x2 = 2

# 导入求解方程组的函数
from scipy.optimize import fsolve

def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1, x1**2 - x2 -2]

result = fsolve(f,[1,1])
print(result)



# 导入积分函数
from scipy import integrate

def g(x):
   return(1 - x**2 ) ** 0.5

pi_2, err = integrate.quad(g, -1, 1)
print(pi_2*2)


