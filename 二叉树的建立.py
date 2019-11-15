#构造二叉树并实现访问操作
#二叉树是一个结点的有限集合，该集合或者为空或者是由一个根结点加上两棵分别称为左子树和右子树的、互不相交的二叉树组成.
#定义中就体现了“递归”的特点.
#二叉树的建立应该是如下过程：首先定义树结点，其次将数据放入树结点，最后再按照某种树的结构将各个结点连接起来.

#定义树节点：
class TreeNode(object):
    def __init__(self,elem = None,lchild = None,rchild = None):
        self.elem = elem #elem是该结点处的数据
        self.lchild = lchild #lchild是该结点处的左子树（又是一个二叉树）
        self.rchild = rchild #rchild是该结点处的右子树（同上）

#定义一颗二叉树，同时命名根结点为root
class Tree():                    
    def __init__(self):
        self.root = TreeNode() #树的根节点root的值默认为None
        self.myQueue = [] #初始化生成一个列表，列表里面的元素就是各个树结点

    def add(self, elem):
        """为树添加节点"""
        node = TreeNode(elem) #将值为elem的元素放入结点中
        if self.root.elem == None: #如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            rootnode = self.myQueue[0] #将此时列表里面的第一个元素作为“根”，这个根应该是某个二叉树结构的根，从这个元素展开，对他的子结构赋值
            if rootnode.lchild == None:
                rootnode.lchild = node
                self.myQueue.append(rootnode.lchild)
            else:
                rootnode.rchild = node
                self.myQueue.append(rootnode.rchild)
                self.myQueue.pop(0) #添加完右结点后将列表里面的第一个元素，即“根”丢弃，于是原来的左结点变成了新的“根”
