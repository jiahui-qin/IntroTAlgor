#红黑树
class RbNode(object):

    def __init__(self, key, color = None, left = None, right = None, p = None):
        self.color = color
        self.key = key
        self.left = left
        self.right = right
        self.p = p #parents        
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



            
