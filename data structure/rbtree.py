'''
红黑树的5个性质
1 每个节点是红色或者黑色
2 根节点是黑色
3 每个叶节点(NIL)是黑色
4 如果一个结点是红色，那么它的两个子节点是黑色
5 对于每个节点，从该节点到其后代所有叶节点的简单路径上，均包含相同数目的黑色节点(黑高相同)
'''

'''
关于python的数据结构实现：指针的处理
指针的作用在于指向一个内容/地址
python里的变量实际上是对象的引用，实际是也就是指向一个实例的指针
下边这个例子就可以看出a.nextnode和b指向的是同一个地址
'''
class Node(object):
    def __init__(self, value, nextnode = None):
        self.value = value
        self.nextnode = nextnode

    def append(self,  n):
        if not isinstance(n, Node):
            n = Node(n)
        self.nextnode = n  ##直接将nextnode指向n
        #n = self.nextnode   
        #self.nextnode.nextnode = n

A = Node(1)
B = Node(2)
A.append(B)
print(A)
print(B)
print(B.value)
print(A.nextnode)
print(A.nextnode.value)
print(A.nextnode.nextnode)
print(B.nextnode)
