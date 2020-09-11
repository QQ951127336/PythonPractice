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

def deleteBST(pre, node, value):
    if node:
        isLeft = None
        if pre:
            if pre.getLeft() == node:
                isLeft = True
            else:
                isLeft = False
        if node.getValue() == value:
            if node.getLeft() is None and node.getRight() is None:
                if pre:
                    if isLeft:
                        pre.leftNode = None
                    else:
                        pre.rightNode = None
                else:
                    return None
            elif node.getLeft() is None:
                if pre:
                    if isLeft:
                        pre.leftNode = node.getRight()
                    else:
                        pre.rightNode = node.getRight()
                else:
                    return node.getRight()
            elif node.getRight() is None:
                if pre:
                    if isLeft:
                        pre.leftNode = node.getLeft()
                    else:
                        pre.rightNode = node.getLeft()
                else:
                    return node.getLeft()
            else:
                tmpNode = node.getLeft()
                while(tmpNode.getRight()):
                    tmpNode = tmpNode.getRight()
                tmpNode.rightNode = node.getRight()
                if pre:
                    if isLeft:
                        pre.leftNode = node.getLeft()
                    else:
                        pre.rightNode = node.getLeft()
                else:
                    return node.getLeft()
        elif node.getValue() < value:
            deleteBST(node, node.getRight(), value)
        else:
            deleteBST(node, node.getLeft(), value)
        return node

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
    root = deleteBST(None, root, 1)
    print("")
    print("------------")
    traversePre(root)
    print("")
    print("------------")
    traverseMid(root)


