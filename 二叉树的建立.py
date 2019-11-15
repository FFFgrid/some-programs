#构造二叉树并实现访问操作
#二叉树是一个结点的有限集合，该集合或者为空或者是由一个根结点加上两棵分别称为左子树和右子树的、互不相交的二叉树组成.
#定义中就体现了“递归”的特点.
#二叉树的建立应该是如下过程：首先定义树结点，其次将数据放入树结点，最后再按照某种树的结构将各个结点连接起来.

#定义树节点：
class TreeNode(object):
    def __init__(self,value = None,lchild = None,rchild = None):
        self.value = value #value是该结点处的数据
        self.lchild = lchild #lchild是该结点处的左子树（又是一个二叉树）
        self.rchild = rchild #rchild是该结点处的右子树（同上）

#定义一颗二叉树，同时命名根结点为root
class Tree():                    
    def __init__(self,value_list): #用一个列表中的元素去初始化树（相当于是层序遍历初始化），如果是#代表该结点处为空
        self.root = TreeNode() #树的根节点root的值默认为None
        self.queue = [] #初始化生成一个列表，列表里面的元素就是各个树结点
        for i in range(len(value_list)):
            self.add(value_list[i])

    def add(self, value):
        """为树添加节点"""
        node = TreeNode(value) #将值为value的元素放入结点中
        if self.root.value == None: #如果树是空的，则对树的根节点赋值
            self.root = node
            self.queue.append(self.root)
        else:
            if value == '#': #当元素值为'#'时，代表该结点不存在
                value = None
          
            root_now = self.queue[0] #将此时列表里面的第一个元素作为“根”，这个根应该是某个二叉树结构的根，从这个元素展开，对他的子结构赋值
            if root_now.lchild == None:
                root_now.lchild = node
                self.queue.append(root_now.lchild)
            else:
                root_now.rchild = node
                self.queue.append(root_now.rchild)
                self.queue.pop(0) #添加完右结点后将列表里面的第一个元素，即“根”丢弃，于是原来的左结点变成了新的“根”

if __name__ == '__main__':
    value = input().split() #该操作就会得到一个列表
    mytree = Tree(value) #用输入的值列表value建立一个树
    for i in range(int(input())):
        try:
            eval(input()) #ex：输入print可直接打印出某个结点处的值
        except:
            print(None) #如果该结点不存在时就输出None
            
            
