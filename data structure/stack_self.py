#栈：stack
## 后进先出，被删除的是最近插入的元素
## 数据结构的实现应该使用 面向对象编程的思想
## 将stack看做一个类(class)，编写一个新类来存放stack

## 总结：可以额外写一个私有的 output 函数来打印这个stack：从0到top-1.这样就不用弹出最后一个元素了
##可以对代码进行完善，将大部分类改为私有类
##https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318650247930b1b21d7d3c64fe38c4b5a80d4469ad7000 
##廖雪峰 python教程 访问限制部分

class stack_self(object):
    
    def __init__(self, value):
        self.value = value  ##value作为一个stack
        self.top = 0

    def retop(self):
        self.top = len(self.value)
        return self.top  ##self.top作为一个指针指向栈的最后一个元素（实际应该减一）

    def isempty(self):
        if self.retop() == 0:
            return True
        else:
            return False
    
    def PUSH(self, x):
        self.top = self.retop() + 1
        self.value.append(x) ##用append方法为最后添加一个元素

    def POP(self):  
        if self.isempty():
            print('no element exists')
        else:
            self.top = self.retop() - 1
            return self.value.pop()  ##用pop方法弹出stack的最后一个元素



stack_test = stack_self([1,34,7,4,2,7,3])
print(stack_test.value)
stack_test.PUSH(5)
print(stack_test.value)
print(stack_test.value)

