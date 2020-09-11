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
        print(node.data)
        traversePre(node.left)
        traversePre(node.right)

def traverseMid(node):
    if node is not None:
        traversePre(node.left)
        print(node.data)
        traversePre(node.right)

def traverseLast(node):
    if node is not None:
        traversePre(node.left)
        traversePre(node.right)
        print(node.data)



