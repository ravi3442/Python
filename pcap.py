#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:00:15 2021

@author: raviravindran
"""

#import pcapy, 
import sys
from struct import *
import ssl
import socket


def ssl_connect():
    
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssock = ssl.wrap_socket(s)
    
    try:
        ssock.connect(("www.google.com",443))
        print(ssock.cipher())
    except:
        print("error")
    
    try:
        ssock.write(b"GET / HTTP/1.1 \r\n")
        ssock.write(b"Host: www.google.com\n\n")
    except Exception as e:
        print("write error: ",e)
    
    data=bytearray()
    try:
        data=ssock.read()
    except Exception as e:
        print("Read Error: ", e)
    
    print(data.decode("utf-8"))

def testfunc(para1, *args, **kwargs):
    print(para1)
    for items in args:
        print(items)

    print(kwargs)
    
    
def testLamda(n):
    return lambda x:x**n
'''
def square(n):
    return testLamda(2)

def cube(n):
    return testLamda(3)
'''

def main(argv):
    """
    devs=pcapy.findalldevs()
    print(devs)   
    pcap_file = pcapy.open_offline("test.pcap")   
    
    count=1
    while count:
        print("Packet #:", count)
        count = count +1
        (header, payload)=pcap_file.next()
        l2hdr = payload[:14]
        l2data = unpack("!6s6sH", l2hdr)
        #print(l2hdr[0])
        #srcmac = "%.2x" % ord(chr(l2hdr[0]))
        #dstmac = "%.2x" % ord(chr(l2hdr[1]))
        srcmac="%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(chr(l2hdr[0])), ord(chr(l2hdr[1])),ord(chr(l2hdr[2])),ord(chr(l2hdr[3])), ord(chr(l2hdr[4])),ord(chr(l2hdr[5])))
        dstmac="%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(chr(l2hdr[6])), ord(chr(l2hdr[7])),ord(chr(l2hdr[8])),ord(chr(l2hdr[9])), ord(chr(l2hdr[10])),ord(chr(l2hdr[11])))
        print("Source MAC", srcmac, "Dest Mac ", dstmac)

    """
    ssl_connect()
    testfunc("ravi", 1, 2, 3, name="Ravi", class_t="5")

    square=testLamda(2)
    cube=testLamda(3)
    print(square(5))
    print(cube(12))    

if __name__ == "__main__":
   main(sys.argv[1:])