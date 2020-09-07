#!/usr/bin/env python
# -*- coding:utf-8 -*-

def binarySearch(dataList, aimValue):
    left = 0
    right = len(dataList) - 1
    while left < right:
        mid = int((left + right)/2)
        if dataList[mid] == aimValue:
            return True
        elif dataList[mid] < aimValue:
            left = mid + 1
        else:
            right = mid - 1
    if dataList[left] == aimValue:
        return True
    return False

if __name__ == '__main__':
    data = [1,2,3,10,12,14,15]
    rawData = [32,2315,12,1345,2]
    rawData.sort()
    print(rawData)
    print(binarySearch(data, 10))
    print(binarySearch(data, 11))
    print(binarySearch(data, 3))