#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:19:38 2021

@author: raviravindran
"""

import ssl, sys
import socket


class test:
    def __init__(self, par1, par2, par3):
        self.name=par1
        self.age=par2
        self.sex=par3
        
    def display(self):
        print(self.name, self.age, self.sex)
        

def main(argv):
    num = [1, 5, 7, 9, 4, 3, 2, 1]
    
    num_list = list(filter(lambda number : number >5, num))
    print(num_list)
    
    data=[['Ravi', 44, 'A'], 
          ['Ramu', 25, 'C'],
          ['Kishan', 33, 'D'],
          ['Jaya', 40, 'A']]
    
    data.sort(key=lambda item: item[1])
    
    print(data)
    
    t1=test("Ravi", "42", "M")
    t1.display();
    
    
    
if __name__ == "__main__":
   main(sys.argv[1:])