#矩阵乘法
#动态规划

def matrix_chain_order(p):
    #p是矩阵乘法中矩阵的维数list
    n = len(p) - 1
    m = [[0 for col in range(n)] for row in range(n)]
    s = [[0 for col in range(n)] for row in range(n)] #初始化两个n*n的矩阵
    for l in range(1, n):
        for i in range(0, n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return [m,s]
chain = [30, 35, 15, 5, 10, 20, 25]
[p,m]] = matrix_chain_order(chain)
print(p)
print(m)

