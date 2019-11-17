def bubblesort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):### 这里i的递增确保了比较可以向后进行
            if alist[i] > alist[i+1]: ### 把大的放到后面
                alist[i],alist[i+1] = alist[i+1],alist[i]

#最简单的冒泡排序的思想是不断进行以下过程：先制定一个比较的范围，一开始从末尾开始，不断和前面的元素比较，把小的元素放在前面；每经过“一轮”比较之后，
#都确保此时列表的最后一个元素是最大的；然后将比较的范围缩小，直到缩到0为止
def short_bubblesort(num_array):
    flag = True
    while flag:
        flag=False
        i=len(num_array)
        for j in range(1,i):
            if num_array[j-1]>num_array[j]:
                num_array[j-1],num_array[j]=num_array[j],num_array[j-1]
                flag=True
            i-=1
