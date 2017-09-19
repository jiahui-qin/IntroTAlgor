##排序算法的分冶法，或者说是迭代排序？
##假设有两堆已经排好序的数组，将它们合并成一组按照顺序排列的数组，每次只需要比较最顶端的数
##归并排序没有做出来

def Merge(A, p, q, r):
    ##A是一个数组，两个已经排好序的数列分别是 L:[p, q] 和 R:[q+1, r]
    L=A[p: q]
    R=A[q: r]
    for k in range(len(A)):
        if len(L) == 0:
            A[k:len(A)] = R
            break
        if len(R) == 0:
            A[k:len(A)] = L
            break
        if L[0] < R[0]:
            A[k] = L[0]
            L.remove(L[0])
        else:
            A[k] = R[0]
            R.remove(R[0])
        
    return(A)

def merge_sort(A, p, r):
    ##对A[p, r]排序
    ##对整个数组进行排序，最后就可以划分为对一个只有2个元素的数组进行 Mrege
    if len(A[p: r])<=1:
        return(A[p: r])
    elif p < r:
        q = int((p+r)/2) ##取中间的数进行划分，int函数完成取整操作
        merge_sort(A, p, q)
        merge_sort(A, q, r)
    return(Merge(A, p, q, r))

A=[4,2,7,8,3,5,7,8,3,5,7,9,3,2,4,6,8,9,4,4,6,3,56,7,8,3,21]
merge_sort(A,0,8)
print(A)