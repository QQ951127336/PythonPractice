#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def int2ip(ipNumber):
    a = (ipNumber >> 24) & 255
    b = (ipNumber >> 16) & 255
    c = (ipNumber >> 8) & 255
    d = (ipNumber) & 255
    return str(a) + "." + str(b) + "." + str(c) + "." + str(d)

def ip2int(ipStr):
    result = 0
    error = -1
    if ipStr is None:
        return error
    strArray = ipStr.split(".")
    if strArray is not None and len(strArray) == 4:
        result = result | (int(strArray[0]) << 24)
        result = result | (int(strArray[1]) << 16)
        result = result | (int(strArray[2]) << 8)
        result = result | (int(strArray[3]))
        return result
    return error


if __name__ == '__main__':
    ipNumber = ip2int('10.3.9.12')
    print(ipNumber)
    print(bin(ipNumber))
    print(int2ip(ipNumber))