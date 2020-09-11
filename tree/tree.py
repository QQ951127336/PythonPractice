#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

    def setLeft(self, value):
        newNode = BiTreeNode(value)
        if self.leftNode is None:
            self.leftNode = newNode
        else:
            newNode.leftNode = self.leftNode
            self.leftNode = newNode

    def setRight(self, value):
        newNode = BiTreeNode(value)
        if self.rightNode is None:
            self.rightNode = newNode
        else:
            newNode.rightNode = self.rightNode
            self.rightNode = newNode

    def getLeft(self):
        return self.leftNode

    def getRight(self):
        return self.rightNode

    def setValue(self, value):
        self.data = value
        
    def getValue(self):
        return self.data

def traversePre(node):
    if node is not None:
        print(node.data, end=" ")
        traversePre(node.getLeft())
        traversePre(node.getRight())

def traverseMid(node):
    if node is not None:
        traverseMid(node.getLeft())
        print(node.data, end=" ")
        traverseMid(node.getRight())

def traverseLast(node):
    if node is not None:
        traverseLast(node.getLeft())
        traverseLast(node.getRight())
        print(node.data, end=" ")

def maxDeep(node):
    if node is not None:
        leftDeep = maxDeep(node.getLeft())
        rightDeep = maxDeep(node.getRight())
        return max(leftDeep, rightDeep) + 1
    return 0

def insertBST(node, value):
    if node:
        if node.getValue() < value:
            if node.getRight():
                insertBST(node.getRight(), value)
            else:
                node.setRight(value)
        elif node.getValue() > value:
            if node.getLeft():
                insertBST(node.getLeft(), value)
            else:
                node.setLeft(value)
        return node
    return BiTreeNode(value)


if __name__ == '__main__':
    root = insertBST(None, 3)
    insertBST(root, 3)
    insertBST(root, 2)
    insertBST(root, 4)
    insertBST(root, 5)
    insertBST(root, 1)
    traversePre(root)
    print("")
    print("------------")
    traverseMid(root)

