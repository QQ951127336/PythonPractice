#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from sort.order import Order
from util.randomUtil import RandomUtil


def partition(dataList, left, right, order=Order.AES):
    if dataList is None or right <= left:
        return None
    factor = 1
    if order == Order.DES:
        factor = -1
    start = left
    midValue = dataList[start]
    left = left + 1
    while left <= right:
        while left <= right and (dataList[left] - midValue) * factor <= 0:
            left = left + 1
        while left <= right and (dataList[right] - midValue) * factor >= 0:
            right = right - 1
        if left <= right:
            dataList[left], dataList[right] = dataList[right], dataList[left]
    dataList[start], dataList[right] = dataList[right], dataList[start]
    return right


def quickSort(dataList, left, right, order=Order.AES):
    if dataList is None:
        return None
    midIndex = partition(dataList, left, right, order)
    if midIndex != None:
        if left != midIndex - 1:
            quickSort(dataList, left, midIndex - 1, order)
        if right != midIndex + 1:
            quickSort(dataList, midIndex + 1, right, order)
    return dataList


if __name__ == '__main__':
    data = RandomUtil().getRandomList(10, 0, 100)
    print(data)
    print("---------------")
    print(quickSort(data, 0, len(data) - 1, Order.AES))
