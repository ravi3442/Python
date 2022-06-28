#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:17:46 2021

@author: raviravindran
"""

import socket
import sys

def main(argv):
    print(socket.gethostbyaddr("8.8.8.8"))
    print(socket.gethostbyname("www.google.com"))
    
    
    if len(sys.argv)!=2:
        port=5000
    else:
        port = int(sys.argv[1])
    
    
    host='localhost'
    mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr=(host, port)
    mysock.connect(addr)
    
    try:
        msg=b"hi, this is a test\n"
        mysock.sendall(msg)
    except socket.errno as e:
        print("Socket error",e)
    finally:
        mysock.close()

if __name__ == "__main__":
   main(sys.argv[1:])