def INSERTION_SORT(orilist, reverse = 'F'):
    ##一个排序算法，reverse=T时将一个数列从低到高依次排列
    ##reverse=F时从高到低依次排列
    for j in range(1, len(orilist)):
        for i in range(0, j):
            if reverse == 'F':
                if orilist[j] < orilist[i]:
                    insert_me(orilist, j, i)
            elif reverse == 'T':
                if orilist[j] > orilist[i]:
                    insert_me(orilist, j, i)
    return orilist


def insert_me(orilist, i, j):
    ##insert_me(orilist, i, j)方法把orilist[i]插入至orilist[j]位置，j<i，中间的都向后移动一位
    key = orilist[i]
    for q in range(i, j, -1):
        orilist[q] = orilist[q-1]
    orilist[j] = key
    return(orilist)

orilist1=[5, 3, 4, 2, 1, 3]
print(INSERTION_SORT(orilist1, reverse='T'), '\n')