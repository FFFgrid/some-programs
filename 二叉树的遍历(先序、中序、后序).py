# 需要用到TreeNode类和Tree类(在二叉树的建立.py中)
# 主要定义了三个遍历函数，实现二叉树的先序、中序、后序遍历（每一种可分为递归实现和非递归实现）
# 访问的顺序仅仅决定于何时访问根结点，即一定是先访问左子树再访问右子树
# 先序(preorder)：根-左-右
# 中序(inorder): 左-根-右
# 后序(postorder): 左-右-根

# 先序遍历的非递归实现
def preorder(root): #root是某个结点，可以是整个树的根结点，也可以是某个子树的根结点
        stack = [root] #借助stack的思想，将右结点先压入栈，左结点后压入栈
        result = [] #result列表用来存放先序遍历结果
        if root == None:
            return 
        while stack:
            root_now = stack.pop()
            if not root_now:
                continue
            result.append(root_now.value)
            stack.append(root_now.rchild)
            stack.append(root_now.lchild)

        return result
        
# 先序遍历的递归实现
def preorder_re(root):
         if root == None:
            return 
        print(root.value，end=' ') #暂时只能遍历过程中每遇到一个元素就输出一个元素(如果不写end就是以一个元素一行的形式输出)
        preorder_re(root.lchild)
        preorder_re(root.rchild)
        
        
# 中序遍历的非递归实现
def inorder(root):
        """ 利用堆栈中序遍历"""
        if root == None:
            return False
        stack = []
        result = [] #
        node = root
        while node or stack:
            while node:  # 从根结点开始，寻找左子树，把它压入栈中
                stack.append(node)
                node = node.lchild
            node = stack.pop()  # while 结束代表前一个没有左子树的结点
            result.append(node.value)
            node = node.rchild  # 然后开始寻找右子树

        return result

#中序遍历的递归实现
def inorder_re(root):
    if root == None:
        return []
    result = []
    result += inorder_re(root.lchild)
    result.append(root.value)
    result += inorder_re(root.rchild)
    return result
        
