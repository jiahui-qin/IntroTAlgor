'''
392. 打劫房屋
假设你是一个专业的窃贼，准备沿着一条街打劫房屋。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

样例
给定 [3, 8, 4], 返回 8.
'''
def houseRobber(A):
    # write your code here
    if len(A) < 2:
        return sum(A)
    else:
        t = [A[0],max(A[0],A[1])]
        for i in range(2, len(A)):
            t.append(max(t[i-1], A[i] + t[i - 2]))

            print(t)
    return max(t)

A = [1,3,2,1,5]
print(houseRobber(A))