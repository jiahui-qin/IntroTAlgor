'''
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

sample:

给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。
'''

#这是一个写的很崎岖的程序，可以说是很暴力了
def sortColors(nums):
    # write your code here
    k = len(nums) - 1
    p = int(sum(nums)/2)
    flag = 0
    try:
        q = 0
        while flag != k :
            print(flag,q) 
            q = q + 1
            if nums[flag] == 1:
                flag = flag + 1
            elif nums[flag] == 0:
                nums.pop(flag)
                nums.insert(0,0)
                while nums[flag] == 0:
                    flag = flag + 1
            else:
                nums.pop(flag)
                nums.append(2)
                if q > k * 2:
                    return nums
        return nums
    except IndexError:
        return nums

print(sortColors([2,0,2,2,1,2,2,1,2,0,0,0,1]))