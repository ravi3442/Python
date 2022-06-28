#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:17:46 2021

@author: raviravindran
"""

import socket

print(socket.gethostbyaddr("8.8.8.8"))
print(socket.gethostbyname("www.google.com"))


host='localhost'
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host, 5555)
mysock.connect(addr)

try:
    msg="hi, this is a test\n"
    mysock.sendall(msg)
except socket.errno as e:
    print("Socket error",e)
finally:
    mysock.close()

