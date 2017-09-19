#排序和顺序统计量  P81
##排序：输入有n个数的数列，输出一个按照从大到小排列的数列
##通常需要排序的是一个数据集的key

##堆排序： p81 -- p94
###  heapsort(A) 函数可以进行排序
###  build_max_heap(A) 函数可以建立一个最大堆
###  max_heapify(A, i) 函数维护最大堆的性质

###二叉树
def max_heapify(A, i):
    ##维护最大堆性质的重要过程，输入为一个数组A和一个下标 i
    ##假设left(i) and right(i) 都是最大堆，但是A(i) 可能小于其孩子
    ##这个函数就是让A[i]逐级下降的过程，以维护最大堆的性质
    
    A.insert(0, 0) ##python计数时时从零开始的
    l = 2 * i #l = left , 这是i的左孩子
    r = 2 * i + 1 #r = right, 这是i的右孩子
    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l
    elif l > len(A) - 1:
        A.remove(A[0])
        return A
    else:
        largest = i
    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r
        

    if largest != i:
        tag = A[largest]
        A[largest] = A[i]
        A[i] = tag
        A.remove(A[0])
        return max_heapify(A, largest)  ##此处参考了http://www.jianshu.com/p/c1dcf423e128 为什么这里要加一个return呢？
    else:
        A.remove(A[0])
        return A



def build_max_heap(A):
    ##建立一个最大堆
    ##采用自下而上的方式：[int(A)/2 + 1 : 1], 可以保证建立一个最大堆
    for i in range(1, int(len(A) / 2) + 1)[::-1]: ##注意这里[::-1]的用法
        max_heapify(A, i) ##对每一个i调用max_heapify
    return A


def heapsort(A):
    ##堆排序的思想：
    ##一个堆中最大的值永远在A[1]的位置上，把A[1]与A[len(A)]互换位置
    ##然后互换位置之后对A[1:len(A)-1]进行build_max_heap
    ##再重复上述过程即可得到一个由小至大的数组
    build_max_heap(A)
    for i in range(1, len(A))[::-1]:
        flag = A[0]
        A[0] = A[i]
        A[i] = flag
        A[:i] = max_heapify(A[:i], 1)
    return A

##测试  
print('将thrlist按照顺序排列: heapsort()')
thrlist = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
print(heapsort(thrlist))

def max_min_trans(A):
    #变换数列的排序方式
    for i in range(int(len(A)/2)):
        flag = A[i]
        A[i] = A[len(A) - i - 1]
        A[len(A) - i - 1] = flag
    return A

##最大优先队列
##有以下4种操作：

def heap_maximum(A):
    #这个函数用来返回 集合A 中的最大值
    ##集合A 必须是一个最大堆
    return A[0]


def heap_extract_max(A):
    #这个函数返回 集合A 的最大值并将其删除
    ##模拟完成有限度最高的任务之后将完成的任务删掉
    if len(A) < 1:
        print('heap underflow') ##错误处理可以改为try···结构
    flag = A[0]
    A.remove(A[0])
    max_heapify(A, 1)
    return flag



def heap_increase_key(A, i, key):
    # 将队列A 中的A[i] 增加至key,这里假设 key > i
    if key < A[i - 1]: ##优先队列里定义的一个队列是从0开始的
        print('new key should bigger than current key')
    A[i - 1] = key
    A.insert(0, float('inf'))  ##插入一个无穷大的值确保永远位于首位
    while i > 0 and A[int(i/2)] < A[i]:
        flag = A[i]
        A[i] = A[int(i/2)]
        A[int(i/2)] = flag
        i = int(i/2)
    A.remove(A[0])
    return A
#测试
print('将thrlist[i]的值增加至key，heap_increase_key(testlist, 4, 17)')
testlist = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
print(heap_increase_key(testlist, 4, 17))


def max_heap_insert(A, key):
    ##在序列A中插入一个元素key，将放置在合适的位置
    A.append(0)
    return heap_increase_key(A, len(A), key)
##测试
print('在序列A中插入一个元素将其放置在格式的位置上， max_heap_insert(testlist, 11)')
testlist = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
print(max_heap_insert(testlist, 11)) 