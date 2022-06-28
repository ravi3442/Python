#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:22:10 2021

@author: raviravindran
"""



def main(argv):
    names =['wine', 'beer', 'pizza', 'burger', 'fries','cola', 'apple'
            ,'donut', 'cake']
    values = [89, 10, 95, 100, 90,79, 50, 10]
    calories =[123, 154, 258, 354, 365, 150, 95, 195]
    foods = buildMenu(names, values, calories)
    testGreedys(foods, 750)    
    

if __name__ == "__main__":
   main(sys.argv[1:])