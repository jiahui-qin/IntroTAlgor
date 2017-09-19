##算法导论 p40 使用分冶算法寻找一个数组的最大子数组
##寻找一个最大子数组可以分为：

def find_max_crossing_subarray(A, low, mid, high):
    ##先寻找一个跨越中点的序列中和最大的数组
    B=A[low: mid] 
    B.reverse()
    left_sum = 0
    left_tag = []
    sumq=0
    for i in range(len(B)): ##先寻找依靠mid中左边最大的值
        sumq = sumq + B[i]
        if sumq > left_sum:
            left_sum = sumq
            left_tag = len(B) - i -1


    right_sum = 0 
    right_tag = 0
    sumq=0
    C = A[mid: high]
    for i in range(len(C)): ##再寻找右边倚靠mid中最大的值
        sumq = sumq + C[i]
        if sumq > right_sum:
            right_sum = sumq
            right_tag = i + mid + 1
    print(left_tag, right_tag, right_sum + left_sum)
    return(left_tag, right_tag, right_sum + left_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return(low, high, A[low])
    else:
        mid = int((low+high)/2)
        [left_low, left_high,left_sum] = find_maximum_subarray(A, low, mid)
        [right_low, right_high, right_sum] = find_maximum_subarray(A, mid, high)
        [cross_low, cross_high, cross_sum] = find_max_crossing_subarray(A, low, mid, high)

        if left_sum > right_sum and left_sum > cross_sum:
            return(left_low, left_high,left_sum )
        elif right_high > left_sum and right_sum > cross_sum:
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)



a=[-2, 2, -3, 4, -1, 2, 1, -5, 3]
print(find_maximum_subarray(a,0,9))