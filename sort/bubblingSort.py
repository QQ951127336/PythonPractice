#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from sort.order import Order
from util.randomUtil import RandomUtil


def bubblingSort(dataList, order=Order.AES):
    factor = 1
    if order == Order.DES:
        factor = -1
    for length in range(len(dataList), 0, -1):
        for index in range(0, length - 1):
            if (dataList[index] - dataList[index + 1]) * factor > 0:
                dataList[index], dataList[index + 1] = dataList[index + 1], dataList[index]
    return dataList


if __name__ == '__main__':
    print(bubblingSort(RandomUtil().getRandomList(10, 0, 100), Order.AES))
