#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:41:15 2021

@author: raviravindran
"""
import socket, sys
import re

def main(argv):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("www.google.com",80))
    
    #http_get=b"GET / HTTP/1.1\nHost:www.google.com\n\n"
    http_get=b"GET / HTTP/1.1\nHost:www.google.com\n\n"
    data=''
    try:
        sock.sendall(http_get)
        data=sock.recvfrom(1024)
    except socket.error:
        print ("Socket error", socket.errno)
    finally:
        print("Closing connection")
        sock.close()
    
    strdata =data[0].decode("utf-8")
    headers=strdata.splitlines()
    
    for s in headers:
        print(s)
        if re.search('Server:',s):
            s=s.replace("Server: ","")
            print(s)

if __name__ == "__main__":
   main(sys.argv[1:])
    