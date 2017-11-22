'''
带备忘的自顶向下法
钢条切割问题，不同的长度有不同的价格，问什么切法使得价值最大
递归可以解决，但是解决的时间复杂度很高
'''

import numpy as np

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
def Memoized_cut_rod(p, n):
    r = [] ##r保存在当前米上切割最大的价格
    for i in range(n):
        r.append(float("-inf"))
    return Memoized_cut_rod_aux(p, n, r)

def Memoized_cut_rod_aux(p, n, r):
    if r[n - 1] > 0: 
        #这是查询操作，如果要查n的时候当前地址有，直接返回这个数值
        return r[n - 1]
    if n == 0:
        #0米时收益为0
        q = 0
    else:
        q = float("-inf")
        for i in range(n):
            q = max(q, p[i] + Memoized_cut_rod_aux(p, n - i - 1, r))
    print(r)
    if n != 10:
        r[n] = q
    else:
        pass
    return r[n]

print(Memoized_cut_rod(p,10))
