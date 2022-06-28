#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:11:49 2022

@author: raviravindran
"""

'''
using dynamic programming to solve a 
problem where given two strings s, t.
The objective is to find the number of insertions
deletion or substitutions required to make {s}={t}

'''

def computeEditDistance(s,t):
    cache={} #(m,n) => result
    def recurse(m,n):
        """
        
        Return the minimum edit distrnace between:
          - first m letters of s
          - first n letters of t
        """
        if(m,n) in cache:
            return cache[(m,n)]
        if m==0: #base case
            result = n
        elif n ==0: #base case
            result =m
        elif s[m-1]==t[n-1]: # last letter matches
            result = recurse(m-1, n-1)
        else:
            subCost = 1 + recurse(m-1, n-1)
            delCost = 1 + recurse(m-1, n)
            insCost = 1 + recurse(m, n-1)
            result = min(subCost, delCost, insCost)
        cache[(m,n)] = result
        return result
            
    return recurse(len(s), len(t))


#print(computeEditDistance('a', 'the cats!'*10))

'''
simple code for gradient descent assuming y=wx

F is known, hence dF is known

'''
points = [(2,4), (4,2), (-1 ,-2)]

def F(w):
    return sum((w*x -y)**2 for x, y in points)

def dF(w):
    return sum(2*(w*x-y)*x for x, y in points)

#Gradient descent
def gradientDescent():
    w=-1
    eta = 0.01
    for t in range(100):
        value = F(w)
        gradient = dF(w)    
        w= w - eta*gradient 
        print('iteration {}: w ={}. F(w)={}'.format(t, w, value))

#gradientDescent()



'''
Code for gradient descent assuming d dimensions

d is known, we generate 100k or more data points

1, 2, 3, 4, 5 is the what we want to achieve using the learning process


'''

# Modelling: what we want to compute

import numpy as np

points = [(np.array([2]), 4), (np.array([4]), 2 )]

print(points)
#d=1

true_w = np.array([1,2,3,4,5])
d= len(true_w)
points = []

for t in range(100000):
    x = np.random.randn(d)
    y  = true_w.dot(x) + np.random.randn()
    #print(x,y)
    points.append((x,y))

def F(w):
    return sum((w.dot(x)-y)**2 for x, y in points)/len(points)

def dF(w):
    return sum(2*(w.dot(x)-y)*x for x, y in points)/len(points)

##########################

#Algorithms : how we compute it
# Gradient descent
def gradientDescent(F, dF, d):
    w=np.zeros(d)
    eta = 0.01
    for t in range(1000):
        value = F(w)
        gradient = dF(w)    
        w= w - eta*gradient 
        print('iteration {}: w ={}. F(w)={}'.format(t, w, value))

#gradientDescent(F, dF, d)


'''
Simple code for stochastic gradient descent assuming d dimensions

Gradient discent scales poorly with the size of the the data set

Stochastic gradient descent addresses the problem by updating the 

w vector only using one of the (x,y) points

'''

def sF(w, i):
    x, y = points[i]
    return (w.dot(x)-y)**2 

def sdF(w,i):
    x, y = points[i]
    return 2*(w.dot(x)-y)*x 

def stochasticGradientDescent(F, dF, d, n):
    w=np.zeros(d)
    eta = 1
    numUpdates=0
    for t in range(1000):
        for i in range (n):
            value = sF(w,i)
            gradient = sdF(w,i)
            numUpdates +=1
            eta = 1.0/numUpdates
            w= w - eta*gradient 
        print('iteration {}: w ={}. F(w)={}'.format(t, w, value))


stochasticGradientDescent(sF, sdF, d, len(points))

