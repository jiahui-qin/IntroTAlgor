##二叉树
##每个节点有4个属性：p(parents)、left、right、key

class NODE(object):
    def __init__(self, value = -1, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Binary_tree(object):

    def __init__(self, key, root):
        #这里可以使用对象的单数组表示方法
        self.key = key
        self.root = root #这个属性指向根节点

    def isempty(self):
        #检查一个树是否为空
        ##删除掉一个节点时，虽然节点保留，但是节点的三个属性全为 -1
        ##直接检查空节点
        #还是检查是否有父节点存在？
        #先写第一种
        if self.root == -1:
            return True
        else:
            return False

    # def print_key(self):
    #     if isempty(self):
    #         return False
    #     else:
    #         def preorder(self.root.key()):
    #             if self.root.key:
    #                 print(self.root.key)
    #                 preorder(self.root.key.left())
    #                 preorder(self.root.key.right())


a=NODE(10,1)
b=NODE(2)

tree=Binary_tree([a,b],0)
print(tree.root)
print(type(tree.key[1]))
print(tree.key[1].value)