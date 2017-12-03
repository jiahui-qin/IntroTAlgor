'''
自底向上的求钢条最佳切割长度
'''
def buttom_up_cut_rod(p, n):
    r = [0, ] ##r保存在当前米上切割最大的价格
    for j in range(n-1):
        r.append(float("-inf"))
        q = float("-inf")
        print(r)
        for i in range(j+1):
            q = max(q, p[i] + r[j - i])
        r[j + 1] = q
    return r[n - 1]

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(buttom_up_cut_rod(p,10))