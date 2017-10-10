##二叉树
##每个节点有4个属性：p(parents)、left、right、key
##这个程序还有很多可以改进的地方：自动排序、插入、删除、对象的分配和释放等等
##有时间再完善吧
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
    def preorder(self,cho_key):
        #先序遍历
        #可以单独拿出来遍历某一个节点的子节点
        if cho_key:
            print(cho_key.value)
            if cho_key.left:
                self.preorder(self.key[cho_key.left])
            if cho_key.right:
                self.preorder(self.key[cho_key.right])
        else:
            return None

    def print_key(self):
        #如果树不为空再进行这个程序
        if self.isempty():
            return False
        else:
            self.preorder(self.key[self.root])
            


a=NODE(10,1,2)
b=NODE(2,3)
c=NODE(4)
d=NODE(6)

tree=Binary_tree([a,b,c,d],0)
#print(type(tree.key[1]))
tree.print_key()
