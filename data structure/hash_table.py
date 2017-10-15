##散列表 算法导论 第11章 p142
"""
散列表(hash table)的查找性能非常好，在完全散列下，可以在O(1)的情况下完成关键字查找
散列表使用一个长度与实际存储的关键字数目成比例的数组来存储(实际存储的关键字数目比全部的可能关键字总数要小的情况下)
不直接把关键字作为数组的下标，而是通过关键字计算出相应的下标
通过链接(chaining)的方法拒绝冲突(collision, 多个关键字映射到数组的同一个下标)

直接寻址表：表中包含所有key的可能取值，取实际关键字时只要取到表中相应的位置即可(直接寻址表本身就可以存放动态集合中的元素)
实际关键字没有的直接将直接寻址表中对于的位置置为空就好

散列表是用一个函数h()将实际关键字映射到散列表的槽中，但是要尽力避免冲突(多个关键字被映射到同一个槽里)
两种方法解决： 1、链接法 2、开放寻址法
散列表的重点是散列函数的设计：一个恰当的散列函数应该关键字的概率分布无关：
除法散列法 h(k)=k modm 除以m取余
乘法散列法 h(k)=m(kA mod 1) 向下取整   (kA mod 1)取kA的小数部分  m选择2的一个幂次， A选择 (sqrt(5)-1)/2
"""
class hashelem(object):
    #哈希表的一个链接
    def __init__(self, key, word):
        self.word = word
        self.key = key


class hashtabe(list):
    #哈希表类

    def hashtable_init(self, k):
        #self定义为一个长度为7的元组(比较安全，不可变)
        #self里的链用列表表示
        self = tuple(self.parper(k))
        return self
    @classmethod 
    def parper(self, k):
        initself = []
        for i in range(k):
            print(i)
            initself.append([])
        return initself

    def hash_insetrt(self, elem):
        #插入一个元素至哈希表
        self[elem.key%7].append(elem)
    
    def hash_find(self, key):
        #输入一个key，寻找这个key对应的word
        for i in self[key%7]:
            if i.key == key:
                return i.word

bb=hashtabe()
bb.hashtable_init(7)
print(bb)

print(bb[1])
bb.hash_insetrt(hashelem(1,1))
print(bb[1])
