##p107 线性时间排序
##p107 排序算法的下界指的是比较排序算法的下界
##接下来的几节介绍了几种线性时间排序的算法，当然不是比较排序

##p108 8.2 计数排序
def counting_sort(A, B, k):
    ##假设n个输入元素中的每一个都是在0到k区间内的一个整数
    ##计数排序的基本思想
    C=[]
    for i in range(k + 1):
        C.append(0)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1 ##C[i]就是数组A中包含i的个数
    
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1] ##有 C[i] 个输入元素小于等于 i
    for j in range(len(A))[::-1]:
        B[C[A[j]] - 1] = A[j] ##有x个输入元素小于或等于i，那么i这个元素就应该放在x个位置，python是从0开始的，所以要 - 1
        C[A[j]] = C[A[j]] - 1
        print(B)
        print(C)
    return B

print(counting_sort([2,5,3,0,2,3,0,3],[10,10,10,10,10,10,10,10],5))