#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:40:15 2021

@author: raviravindran
"""

import http.client, sys


def main(argv):
    h= http.client.HTTPConnection("www.google.com")
    h.request("GET", "/")
    data = h.getresponse()
    print(data.code)
    print(data.headers)
    text = data.readlines()
    
    for t in text:
        print(t.decode('utf-8'))
        #print(t)

if __name__ == "__main__":
   main(sys.argv[1:])