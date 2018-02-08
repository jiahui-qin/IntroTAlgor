# 2018/2/8
## 没想到lintcode居然会清空我以前做的题！以后自己做的题都要复制到本地啦
'''
78. 最长公共前缀
给k个字符串，求出他们的最长公共前缀(LCP)

在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"

在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"

思路大概就是自己写一个函数来单独对比两个字符串的LCP，全对比一遍就结束了
'''

class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        tar = self.comstr(strs[0], strs[1])
        for i in range(1,len(strs)):
            print(i, tar, strs[i])
            tar = self.comstr(tar, strs[i])
        return tar
        
    
    def comstr(self, str1, str2):
        # 返回两个字符串相同的前缀
        if len(str1) <= len(str2):
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return str1[0 : i]
            return str1
        else:
            for i in range(len(str2)):
                if str1[i] != str2[i]:
                    return str1[0 : i]
            return str2
        
        
