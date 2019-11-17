#利用二叉树的建立.py文件里面定义的TreeNode类和Tree类
#结合二叉树的遍历(先序、中序、后序).py的思想

#先序中序推层序（其实这里的重点是如何利用先序和中序的结果推出树的结构）

def builttree(preorder_result, inorder_result):
        # write code here
        if len(preorder_result)==0:
            return 
        root=TreeNode(preorder_result[0]) #preorder_result[0]就是整个树的根
        Index=inorder_result.index(preorder_result[0]) #在中序遍历结果中找到整个树的根对应的下标序号
        root.lchild=builttree(preorder_result[1:Index+1], inorder_result[0:Index]) #中序遍历结果的前Index个元素就是根的左子树，与之对应的先序遍历结果就是preorder_result[1:Index+1]
        root.rchild=builttree(preorder_result[Index+1:], inorder_result[Index+1:])
        return root

def show(root): #以层序遍历的形式输出
    # write code here
    outList=[]
    queue=[root]
    while queue!=[] and root:
        outList.append(queue[0].value)
        if queue[0].lchild!=None:
            queue.append(queue[0].lchild)
        if queue[0].rchild!=None:
            queue.append(queue[0].rchild)
        queue.pop(0)
    return outList

if __name__ == '__main__':
    
    result = (show(builttree(input().split(),input().split())))
    print(' '.join(result))


