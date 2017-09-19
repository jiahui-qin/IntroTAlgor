##第七章 快速排序 
##p95
###快速排序的平均性能非常好，期望时间复杂度是O(n lgn)，原址排序
###对于这个算法的理解参考了  http://blog.csdn.net/morewindows/article/details/6684558
###还有随机快速排序没有看

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return A

def partition(A, p, r):
    ##通过这个过程将数组A划分为以下3个部分
    #主元，并返回主元的位置
    ##左侧，全部小于主元
    ##右侧，全部大于主元
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            flag = A[i]
            A[i] = A[j]
            A[j] = flag
    flag2 = A[i + 1]
    A[i + 1] = A[r]
    A[r] = flag2
    return i + 1
A=[8,7,6,5]
print(quick_sort(A, 1, 3))
