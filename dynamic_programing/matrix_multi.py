#矩阵乘法
#动态规划

def matrix_chain_order(p):
    #p是矩阵乘法中矩阵的维数list
    n = len(p) - 1
    num = [[0 for col in range(n)] for row in range(n)]
    step = [[0 for col in range(n)] for row in range(n)] #初始化两个n*n的矩阵
    for l in range(1, n):
        for row in range(0, n - l ):
            col = row + l
            num[row][col] = float("inf")
            for k in range(row, col):
                q = num[row][k] + num[k + 1][col] + p[row] * p[k + 1] * p[col + 1]
                if q < num[row][col]:
                    num[row][col] = q
                    step[row][col] = k + 1
    return [num,step]

def print_optimal(step, i, j):
    print(i,j)
    if i == j:
        print('A' + i, end='')
    else:
        print("(", end='')
        print_optimal(step, i, step[i][j])
        print_optimal(step, step[i][j] + 1, j)
        print(")", end='')


chain = [30, 35, 15, 5, 10, 20, 25]
[num,step] = matrix_chain_order(chain)
print(num)
print(step)
print_optimal(step, 0,5)

