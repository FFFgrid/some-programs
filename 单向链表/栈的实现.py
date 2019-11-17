class _node:
    __slots__ = '_element','_next'#用__slots__可以提升内存应用效率

    def __init__(self,element,next):
        self._element = element #该node处的值
        self._next = next #下一个node的引用       

class LinkedStack:
    def __init__(self):
        """create an empty Stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of thr elements in the stack"""
        return self._size()

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    
    def push(self,e):
        """Add an element e to the top of the stack"""
        self._head = _node(e,self._head) #当一个元素的next指向当前的head时，说明他就是新的head
        self._size += 1

    def top(self):
        """Return the element at the top of the stack"""
        if self.is_empty():
            print('Stack is empty')
        else:
            return self._head._element
    
    def pop(self):
        """Return and remove the element from the top of the stack"""
        if self.is_empty():
            print('Stack is empty')
        else:
            ans = self._head._element #get the value
            self._head  =self._head._next #bypass the former top node 
            self._size -= 1
            return ans
