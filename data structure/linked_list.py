#链表的实现：
##链表的每一个key都有一个prev和一个next指向前一个和后一个元素
##在第一个和最后一个元素的前后可以添加一个哨兵，将这两个元素的prev和next分别指向哨兵
##这样做可以优化链表的代码

#指针和对象的实现
##可以用一个三维数组来保存链表，三维分别是next、key、prev
##也可以使用一个一维数组来表示，第i个元素是key的话，第i+1个元素就是prev，第i+2个元素就是next
##由于添加或删除元素的时候只需要修改元素的指针即可，删除的时候就会留下冗余
##于是我们可以用p136的方法来对对象进行分配和释放
##用一个自由表来指向冗余的对象