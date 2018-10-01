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


def dye_x(res0, index, p, cube, mul=1):
    global total
    p0 = p
    c = cp(cube)
    res = cp(res0)
    e = edges[index]
    tmp = p[0]+e*mul
    if tmp < 0 or tmp > 2:
        return False

    p = (p[0]+mul, p[1], p[2])
    if c[p] == 1:
        return False

    c[p] = 1
    if e == 2:
        p = (p[0]+mul, p[1], p[2])
        if c[p] == 1:
            return False
        c[p] = 1

    if index == n-1:
        total += 1
        res.append('x%s%d, %s' % ('+' if mul > 0 else '-', edges[index], p0))
        print('*'*40, total)
        print("\n".join(res))
        return True

    #print('%02d: %d x%s' % (index, e, '+' if mul > 0 else '-'))
    res.append('x%s%d, %s' % ('+' if mul > 0 else '-', edges[index], p0))
    add(res, index+1, p, c)


def dye_y(res0, index, p, cube, mul=1):
    global total
    p0 = p
    c = cp(cube)
    res = cp(res0)
    e = edges[index]
    tmp = p[1]+e*mul
    if tmp < 0 or tmp > 2:
        return

    p = (p[0], p[1]+mul, p[2])
    if c[p] == 1:
        return False

    c[p] = 1
    if e == 2:
        p = (p[0], p[1]+mul, p[2])
        if c[p] == 1:
            return False
        c[p] = 1

    if index == n-1:
        total += 1
        res.append('y%s%d, %s' % ('+' if mul > 0 else '-', edges[index], p0))
        print('*'*40, total)
        print("\n".join(res))
        return

    #print('%02d: %d y%s' % (index, e, '+' if mul > 0 else '-'))
    res.append('y%s%d, %s' % ('+' if mul > 0 else '-', edges[index], p0))
    add(res, index+1, p, c)


def dye_z(res0, index, p, cube, mul=1):
    global total
    p0 = p
    c = cp(cube)
    res = cp(res0)
    e = edges[index]
    tmp = p[2]+e*mul
    if tmp < 0 or tmp > 2:
        return

    p = (p[0], p[1], p[2]+mul)
    if c[p] == 1:
        return False

    c[p] = 1
    if e == 2:
        p = (p[0], p[1], p[2]+mul)
        if c[p] == 1:
            return False
        c[p] = 1

    if index == n-1:
        total += 1
        res.append('z%s: %d, %s' % ('+' if mul > 0 else '-', edges[index], p0))
        print('*'*40, total)
        print("\n".join(res))
        return

    #print('%02d: %d z%s' % (index, e, '+' if mul > 0 else '-'))
    res.append('z%s%d, %s' % ('+' if mul > 0 else '-', edges[index], p0))
    add(res, index+1, p, c)


def add(res, index, p, cube):
    dye_x(res, index, p, cube, 1)
    dye_x(res, index, p, cube, -1)
    dye_y(res, index, p, cube, 1)
    dye_y(res, index, p, cube, -1)
    dye_z(res, index, p, cube, 1)
    dye_z(res, index, p, cube, -1)


cube = np.zeros((3,3,3), dtype=np.int)  # 魔方矩阵初始化
p = (0,0,0)
cube[p] = 1
res = []
dye_z(res, 0, p, cube)
cube[p] = 0
