def longestCommonSubsequence(A, B):
    # write your code here
    m = len(A)
    n = len(B)
    c = [[0 for col in range(n + 1)] for row in range(m + 1)]
    print(c)
    for i in range(1, m+1):
        for j in range(1, n+1):
            print(i,j)
            print(c[i-1][j],c[i][j-1])
            if A[i - 1] == B[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
            print(c)
    return c[m][n]

A="ASD"
B="AS"
print(longestCommonSubsequence(A,B))