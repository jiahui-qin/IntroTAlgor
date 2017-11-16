#红黑树
class RbNode(object):

    def __init__(self, key, color = None, left = None, right = None, parents = None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.parents = parents       
    ##再建一个类还是直接在这个类里边写？好像可以直接在这个类里边写

class RbTree(object):
    def __init__(self, rblist = None, root = None):
        self.rblist = rblist
        self.root = root
        self.Nil = None

    def rb_tree_search(self, s_key, start_key):
        #在self树里搜索s_key关键字,start_key为开始搜索的字(可以先指定一个范围,start_key默认值应该是root)
        if s_key == start_key.key:
            return start_key
        if s_key < start_key.key:
            return self.rb_tree_search(s_key, start_key.left)
        else:
            return self.rb_tree_search(s_key, start_key.right)

    def iterative_tree_search(self, s_key, start_key):
        #用while循环搜索，效率更高
        while s_key != start_key.key:
            if s_key < start_key.key:
                start_key = start_key.left
            else:
                start_key = start_key.right
        return start_key

    def cal_bh(self, cal_node):
        #计算cal_node节点的黑高
        Sum = 1
        while cal_node:
            if cal_node.color == 'black':
                Sum = Sum + 1
            cal_node = cal_node.right
        return Sum

    def Left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.Nil:
            y.left.parents = x
        y.parents = x.parents
        if x.parents == self.Nil:
            self.root = y
        elif x == x.parents.left:
            x.parents.left = y
        else:
            x.parents.right = y
        y.left = x
        x.parents = y

    def right_rotate(self, y):
        #右旋操作
        x = y.left
        y.left = x.right
        if x.left !=self.Nil:
            x.right.parents = y
        x.parents = y.parents
        if y.parents == self.Nil:
            self.root = x
        elif y == y.parents.left:
            y.parents.left = x
        else:
            y.parents.right = x
        x.right = y
        y.parents = x

    def RB_insert(self, z):
        y = self.Nil
        x = self.root
        while x != self.Nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parents = y
        if y == self.Nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.Nil
        z.right = self.Nil
        z.color =  'RED'
        #self.RB_insert_fixup(z)
    
    def RB_insert_fixup(self,z):
        while z.parents.color == 'red':
            if z.parents 
        

a = RbNode(18)
tree = RbTree()
tree.RB_insert(a)
b = RbNode(16)
tree.RB_insert(b)
print(tree.root.left.key)
c = RbNode(15)
tree.RB_insert(c)
print(tree.root.left.left.key)
d = RbNode(17)
tree.RB_insert(d)
print(tree.root.left.right.key)


# def main():
#     print('dd')
#     d = RbNode(14,'b',None,None,c)
#     e = RbNode(19,'b',None,None,c)
#     a = RbNode(11,'b',b,c)
#     b = RbNode(9,'b',None,None,a)
#     c = RbNode(18,'b',d,e,a)
#     tree = RbTree([a,b,c,d,e],a)
#     tree.Left_rotate(a)
#     print(b.left.key)

# if __name__ == "__name__":
#     main()