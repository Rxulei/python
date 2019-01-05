# Created by: xulei
# Created on: 2018/12/27

i = 1
while i <= 9:
    j = 1
    while j <= i:
        s = i * j
        print("%d*%d = %d " % (i, j, s), end="\t")  # 当有连续的值要输出 用%（i,j,s）
        j += 1                             # 当不想换行时，用end="" 两个引号之间可以加内容
                                           # 也可以空格  \t 的作用是垂直方向上对齐
    i += 1
    print("")      # 就是换行作用
