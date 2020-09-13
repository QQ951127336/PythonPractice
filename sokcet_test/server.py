#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
TAG = "CLIENT : "

def log(*message):
    print(TAG, message)

def startServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1',80))
    s.listen()
    c, addr = s.accept()
    log("come from client address :", addr)
    c.send("I am server".encode('utf-8'))
    log(c.recv(2048))
    c.close()

if __name__ ==  '__main__':
    startServer()