# LintCode刷题总结

这里总结一些刷题出来的，平常没有积累到的，有助于提高算法效率或者什么稀奇古怪的实现方法啦。

好像平常刷完一道题写在后边很难翻出来的感觉，还是记在这里比较方便啦。

1. 递归还不是很熟

1. 当list里去掉重复元素的时候之前用的是 *lll = list(set(lll))*, 查资料之后说 *{}.fromkeys(nums).keys()* 应该比较快

1. 二进制的相关操作： bin()将一个十进制数转化为二进制， 求补码： *bin(2 \*\* 32 + number)* 32是给定整数的位数

1. 少用条件跳转语句，比如break, continue等等等

1. int()方法会舍去小数部分，比如 *int(2.9) = 2*，用int做条件的时候可能取不到中间的某个数字

1. 判断奇数偶数的时候要用*(num%2) == 0*就是偶数啦

1. 不再额外创建list，选择可以重复使用的int有助于降低空间复杂度

1. 开方的时候可以用 *int \*\* 0.5* 或者用math包的sqrt函数

1. 记一下常用的list操作方法 切片 append count统计某元素出现的个数 extend用新列表扩展就列表 index在列表中找出某个值匹配的第一项 insert(index, obj) pop(obj = list[-1])默认删最后一个元素 remove(obj)删掉某个值的第一个匹配项 reverse反向 sort排序

1. string操作 string不能直接修改， string.count(str, beg = 0, end = len(string)) string.find(str, beg, end)

1. 要建立一个矩阵的话可以用这个方法来建立，[[0 for col in range(n)] for row in range(n)]，除此之外numpy应该也有函数用来建立一个矩阵

1. 字符串常用操作方法