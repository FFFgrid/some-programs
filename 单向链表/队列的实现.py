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
        
    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            print('Queue is empty')
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ans

    def enqueue(self,e):
        """Add an element to the back of the queue"""
        newest = self._Node(e,None) #this node will be the tail node
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest #Update reference to tail node
        self._size += 1
