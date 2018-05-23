def canJump(A):
    # write your code here
    A_len = len(A)
    A_mat = [0 for col in range(A_len)]
    for i in range(1,A[0] + 1):
        A_mat[i] = 1
    for i in range(A_len - 1):
        if A_mat[i] == 1:
            for j in range(1,A[i] + 1):
                A_mat[i + j] = 1
                if A_mat[A_len - 1] == 1:
                    return 'True'
            A_mat[i] = 0
    if A_mat[A_len - 1] == 1:
        return 'True'
    else:
        return 'False'

A = [4,6,9,5,9,3,0]
print(canJump(A))