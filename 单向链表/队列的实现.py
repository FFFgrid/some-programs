class _node:
    __slots__ = '_element','_next'#用__slots__可以提升内存应用效率

    def __init__(self,element,next):
        self._element = element #该node处的值
        self._next = next #下一个node的引用       

class LinkedQueue:
    """First In First Out"""
    def __init__(self):
        """create an empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of thr elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    
    def first(self):
        """Return(don't remove the element at the front of the queue )"""
        if self.is_empty():
            print('Queue is empty')
        else:
            return self._head._element
