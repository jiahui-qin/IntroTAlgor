def MINIMUM(A):
    ##在一个数组中查找最小值
    ##每一个元素和后一个元素比较，保留最小的元素
    ##比较 n-1 次
    minA = A[0]
    for i in range(1, len(A)):
        if minA > A[i]:
            minA = A[i]
    return minA

print(MINIMUM([9,8,7,6,5,4,3,2]))



def minandmax(A):
    ##同时取出一个数组的最大值和最小值
    ##这个函数确认len(A)是奇数还是偶数并返回最后的结果
    if len(A) % 2 ==1:#len(A)为奇数时min和max都设定为A[0]
        minA = A[0]
        maxA = A[0]
        return compare_2(A, 1, minA, maxA)
    else:
        if A[0] > A[1]:
            maxA = A[0]
            minA = A[1]
        else:
            maxA = A[1]
            minA = A[0]
        return compare_2(A, 2, minA, maxA)

def compare_2(A, num, minA, maxA):
    ##每两组元素比较3次
    for i in range(num, len(A))[::2]:  ##元素的切片特性
        if A[i] > A[i + 1]:
            maxA = max([maxA, A[i]])
            minA = min([minA, A[i + 1]])
        else:
            maxA = max([maxA, A[i + 1]])
            minA = min([minA, A[i]])
    return maxA, minA


print(minandmax([9,8,7,6,5,4,3,2]))