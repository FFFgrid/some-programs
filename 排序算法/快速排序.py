def quicksort(seq):
    if len(seq) < 2: #当序列只有一个元素时就不需要排序
        return seq
    else:
        base = seq[0] #核心思想就是找一个数作为一个基准数(可以直接取第一个数)，将剩下的数分为比基准小的(left)和比基准大的(right)两组
        left = [elem for elem in seq[1:] if elem < base]
        right = [elem for elem in seq[1:] if elem > base]
        return quicksort(left) + [base] + quicksort(right) #利用递归循环此过程
    
