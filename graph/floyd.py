#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def floydShortestPath(dataMatrix, startIndex, endIndex):
    if dataMatrix is None:
        return None
    length = len(dataMatrix)
    for mid in range(0, length):
        for start in range(0, length):
            for end in range(0, length):
                if dataMatrix[start][mid] is not None and dataMatrix[mid][end] is not None:
                    path = dataMatrix[start][mid] + dataMatrix[mid][end]
                    if dataMatrix[start][end] is None or path < dataMatrix[start][end]:
                        dataMatrix[start][end] = path
    return dataMatrix[startIndex][endIndex]
