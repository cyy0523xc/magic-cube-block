# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年10月01日 星期一 21时09分30秒
import numpy as np
from copy import deepcopy as cp

edges = '3 3 3 3 2 2 2 3 3 2 2 3 2 3 2 2 3'
edges = [int(i)-1 for i in edges.split()]  # 边
n = len(edges)  # 边的数量
total = 0
print("total edges: ", n)

# 三个旋转方向的单位
rotate_unit = [
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1)
]

# 旋转方向
label = ['x', 'y', 'z']


def dyeing(res0, p0, rotate, index, cube, mul=1):
    """
    Args:
        res0: 结果
        p0: 当前节点
        rotate: 旋转方向，取值0,1,2
    """
    p = p0
    e = edges[index]
    tmp = p[rotate]+e*mul
    if tmp < 0 or tmp > 2:
        return

    c = cp(cube)
    unit_mul = 1 if mul > 0 else -1
    unit = rotate_unit[rotate]
    p = tuple(x+y*unit_mul for x, y in zip(p, unit))
    if c[p] == 1:
        return False

    c[p] = 1
    new_point = [p]
    if e == 2:
        p = tuple(x+y*unit_mul for x, y in zip(p, unit))
        if c[p] == 1:
            return False
        c[p] = 1
        new_point.append(p)

    global total
    res = cp(res0)
    if index == n-1:
        total += 1
        res.append('%s -> %s%s%d -> %s' % (p0, label[rotate], '+' if mul > 0 else '-', edges[index], new_point))
        print('*'*40, total)
        print("\n".join(res))
        return

    res.append('%s -> %s%s%d -> %s' % (p0, label[rotate], '+' if mul > 0 else '-', edges[index], new_point))
    add(res, index+1, p, c)


def add(res, index, p, cube):
    # def dyeing(res0, p0, rotate, index, cube, mul=1):
    dyeing(res, p, 0, index, cube, 1)
    dyeing(res, p, 0, index, cube, -1)
    dyeing(res, p, 1, index, cube, 1)
    dyeing(res, p, 1, index, cube, -1)
    dyeing(res, p, 2, index, cube, 1)
    dyeing(res, p, 2, index, cube, -1)


cube = np.zeros((3, 3, 3), dtype=np.int)  # 魔方矩阵初始化
p = (0, 0, 0)
cube[p] = 1
# def dyeing(res0, p0, rotate, index, cube, mul=1):
dyeing([], p, 2, 0, cube, 1)
