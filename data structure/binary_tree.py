##二叉树
##每个节点有4个属性：p(parents)、left、right、queue
##这个程序还有很多可以改进的地方：自动排序、插入、删除、对象的分配和释放等等
##有时间再完善吧
class NODE(object):
    ##NODE类的left和right属性由程序自动指定
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.left = None
        self.right = None

class Binary_tree(object):

    def __init__(self, root = None):
        #这里可以使用对象的单数组表示方法
        self.queue = []  #queue这个序列就是NODE序列
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

    def preorder(self,cho_queue):
        #先序遍历:先输出父节点，再输出子节点
        #可以单独拿出来遍历某一个节点的子节点
        if cho_queue:
            print(cho_queue.value)
            if cho_queue.left:
                self.preorder(self.queue[cho_queue.left])
            if cho_queue.right:
                self.preorder(self.queue[cho_queue.right])
        else:
            return None

    def inorder(self, cho_queue):
        #中序遍历：父节点总是在左子节点和右子节点的中间
        if cho_queue:
            if cho_queue.left:
                self.inorder(self.queue[cho_queue.left])
            print(cho_queue.value)
            if cho_queue.right:
                self.inorder(self.queue[cho_queue.right])
        else:
            return None

    def postorder(self, cho_queue):
        #后序遍历：父节点总是在左子节点和右子节点之后
        if cho_queue:
            if cho_queue.left:
                self.inorder(self.queue[cho_queue.left])
            if cho_queue.right:
                self.inorder(self.queue[cho_queue.right])
            print(cho_queue.value)
        else:
            return None

    def tree_insert(self, node):
        self.queue.append(node)
        ##插入节点
        if not self.root:
            self.root = node
        else:
            y = None
            x = self.root  
            while x:
                y = x
                if x.left
                    if self.queue[x.left].key < x.key:
                        x = self.queue[x.left]
                    else:
                        if x.right
                            x = self.queue[x.right]
        if node.key < y.key:
                y.left = len(self) - 1
            else:
                y.right = len(self) - 1




a=NODE('wo',4)
b=NODE('cao',3)
c=NODE('ni',6)
d=NODE('ma',1)

tree=Binary_tree()
tree.tree_insert(a)
print(tree.root.value)
tree.tree_insert(b)
tree.tree_insert(c)
tree.tree_insert(d)
tree.preorder()
