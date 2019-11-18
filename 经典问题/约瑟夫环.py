def josephus(num, k, m):
    """
    约瑟夫环（约瑟夫问题）是一个数学的应用问题：
    已知num个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。
    从编号为k的人开始报数，数到m的那个人出列；
    他的下一个人又从1开始报数，数到m的那个人又出列；
    依此规律重复下去，直到圆桌周围的人全部出列。
    :param num:总人数
    :param k:开始的编号
    :param m:数到m的出列
    :return:
    """
    alist = [x + 1 for x in range(num)] # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    

    index, step = k-1, m  # 从1号开始报数，数到3的那个人出列
    while len(alist) > 1:
        index = (index + step - 1) % len(alist)  # 最关键的一步
        print('出去的数：', alist[index])
        # del alist[index]
        alist.pop(index)
    return '最后的一个数：%s' % alist[0]
