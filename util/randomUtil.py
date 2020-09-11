#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random


class RandomUtil():

    def getRandomList(self, length, min, max):
        data = []
        while (length > 0):
            data.append(random.randint(min, max))
            length = length - 1
        return data


if __name__ == '__main__':
    randomUtil = RandomUtil()
    print(randomUtil.getRandomList(10, 0, 10000))
