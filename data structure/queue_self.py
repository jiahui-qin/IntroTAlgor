class queue_self(object):
    def __init__(self,value):
        self.value = value
        self.tail = 0
        self.head = 0

    def re_tail(self):  
        #更新self.tail
        self.tail = len(self.value) - 1
        return self.tail

    def is_empty(self):
        if self.re_tail() == self.head:
            return True
        else:
            return False

    def enqueue(self, x): 
        ##往队列中加入新元素x
        self.value.append(x)
        self.re_tail() ##更新一次tail的值
        return self

    def dequeue(self): 
        ##队列中的第一个元素先出去
        if self.is_empty():
            print("no element exists")
        else:
            self.head = self.head + 1
            #return self.value(self.head - 1)

    def get_queue(self):
        return self.value[self.head:self.tail+1] #用切片操作输出queue

queue_test = queue_self([2,3,4,6,7,2,4,5])

print(queue_test.value)
print(queue_test.re_tail())
queue_test.dequeue()
print(queue_test.get_queue())
queue_test.enqueue(2)
print(queue_test.get_queue())