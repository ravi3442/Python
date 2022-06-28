#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:15:42 2021

@author: raviravindran
"""

import socket
import sys


def main(argv):
    size=512
    host=''
    port=9898
    
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    if len(sys.argv)!=2:
        port=9898
    else:
        port = int(sys.argv[1])
    
    sock.bind((host, port))
    sock.listen(5)
    
    c, addr=sock.accept()
    data = c.recv(size)
    if data:
        f=open("./storage.dat", "+a")
        print("Connection from: ", addr[0])
        f.write(addr[0])
        f.write(":")
        f.write(data.decode("utf-8"))
        f.close()
    sock.close()
    
if __name__ == "__main__":
   main(sys.argv[1:])