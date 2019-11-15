#构造二叉树并实现访问操作
#二叉树是一个结点的有限集合，该集合或者为空或者是由一个根结点加上两棵分别称为左子树和右子树的、互不相交的二叉树组成.
#定义中就体现了“递归”的特点.
#二叉树的建立应该是如下过程：首先定义树结点，其次将数据放入树结点，最后再按照某种树的结构将各个结点连接起来.

#定义树节点：
class Node(object):
    def __init__(self,elem = None,lchild = None,rchild = None):
        self.elem = elem #elem是该结点处的数据
        self.lchild = lchild #lchild是该结点处的左子树（又是一个二叉树）
        self.rchild = rchild #rchild是该结点处的右子树（同上）

#定义一颗二叉树，同时命名根结点为root
class MyTree():                    
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == None:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此节点丢弃
