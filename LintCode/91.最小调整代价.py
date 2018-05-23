'''
描述
给一个整数数组，调整每个数的大小，使得相邻的两个数的差不大于一个给定的整数target，调整每个数的代价为调整前后的差的绝对值，求调整代价之和最小是多少。

你可以假设数组中每个整数都是正整数，且小于等于100。

样例
对于数组[1, 4, 2, 3]和target=1，最小的调整方案是调整为[2, 3, 2, 3]，调整代价之和是2。返回2。
'''
def MinAdjustmentCost(A, target):
    # write your cod here
    A_len = len(A)
    f = [[ float('inf') for j in range(10)] for i in range(A_len+1)]
    for i in range(10):
        f[0][i] = 0
    for i in range(1, A_len+1):
        for j in range(10):
            if f[i - 1][j] != float('inf'):
                for k in range(10):
                    if abs(j - k) <= target:
                        f[i][k] = min(f[i][k], f[i-1][j] + abs(A[i-1]-k))
        print(f)
    ans = f[A_len][9]
    for i in range(10):
        if f[A_len][i] <  ans:
            ans = f[A_len][i]
    return ans

A = [1,4]
target = 2
print(MinAdjustmentCost(A, target))