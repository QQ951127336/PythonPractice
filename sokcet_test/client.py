#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
TAG = "SERVER : "

def log(*message):
    print(TAG, message)

def startClient():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1',80))
    s.send("I am from client".encode('utf-8'))
    log(s.recv(2048))
    s.close()

if __name__ ==  '__main__':
    startClient()