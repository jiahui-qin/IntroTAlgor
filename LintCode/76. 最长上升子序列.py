'''
最长上升子序列的定义：

最长上升子序列问题是在一个无序的给定序列中找到一个尽可能长的由低到高排列的子序列，这种子序列不一定是连续的或者唯一的。
https://en.wikipedia.org/wiki/Longest_increasing_subsequence

样例
给出 [5,4,1,2,3]，LIS 是 [1,2,3]，返回 3
给出 [4,2,4,5,3,7]，LIS 是 [2,4,5,7]，返回 4
'''
def longestIncreasingSubsequence(nums):
    # write your code here
    num_len = len(nums)
    lis = [1,]
    for i in range(1,num_len):
        cur = 0
        for j in range(0, i):
            if nums[i] > nums[j]:
                if lis[j] > cur:
                    cur = lis[j]
        lis.append(cur + 1)
    print(lis)
    return lis[num_len - 1]


a = [88,4,24,82,86,1,56,74,71,9,8,18,26,53,77,87,60,27,69,17,76,23,67,14,98,13,10,83,20,43,39,29,92,31,0,30,90,70,37,59]
print(longestIncreasingSubsequence(a))