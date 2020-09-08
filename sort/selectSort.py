#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sort.order import Order
from util.randomUtil import RandomUtil


def selectSort(dataList, order=Order.AES):
    if dataList is None:
        return None
    length = len(dataList)
    factor = 1
    if order == Order.DES:
        factor = -1
    for start in range(0, length - 1):
        for index in range(start + 1, length):
            if (dataList[start] - dataList[index]) * factor > 0:
                dataList[start], dataList[index] = dataList[index], dataList[start]
    return dataList

if __name__ == '__main__':
    print(selectSort(RandomUtil().getRandomList(10, 0, 100)))
    print(selectSort(RandomUtil().getRandomList(10, 0, 100), Order.DES))

