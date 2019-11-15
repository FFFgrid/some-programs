# 构造二叉树并实现访问操作
二叉树是一个结点的有限集合，该集合或者为空或者是由一个根结点加上两棵分别称为左子树和右子树的、互不相交的二叉树组成.
定义中就体现了“递归”的特点.
二叉树的建立应该是如下过程：首先定义树结点，其次将数据放入树结点，最后再按照某种树的结构将各个结点连接起来.

定义树节点：
class Node(object):
    def __init__(self,elem = None,lchild = None,rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
