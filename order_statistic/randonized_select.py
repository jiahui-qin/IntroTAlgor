import sys
sys.path.append('F:\IntroTAlgor\sort')
import quick_sort
A=[8,7,6,5,2,5,8,5,3,3]
print(quick_sort.quick_sort(A, 0, 7))

def randomized_select(A, p, r, i):
    ##线性选择算法
    ##在数组A中选择出元素x，它大于A中i-1个元素
    ##时间复杂度为 O(n)
    if len(A) == 1:
        return A
    q = quick_sort.randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)

print(randomized_select(A, 0, 7, 8))