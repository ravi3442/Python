#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:59:08 2021

@author: raviravindran
"""
import math
import tensorflow as tf

def calculateBitErrorRate(packetErrorRate):
    packetSize= 100*8
    codeRate=0.25
    
    codeBlockSize=packetSize/codeRate
    
    print("The Code Block Size is: ", codeBlockSize)
    
   # print("Log test ", math.log(10000,100))
    
    temp =(1-packetErrorRate)** (1/codeBlockSize)

    print("Temp ", temp)
    
    bitErrorRate= 1- temp
    
    print("The BER is ", bitErrorRate)


def calculatePacketErrorRate(bitErrorRate):
    packetSize= 100*8
    codeRate=0.25
    
    codeBlockSize=packetSize/codeRate
    
    temp = (1-bitErrorRate)**codeBlockSize
    
    packetErrorRate= 1-temp
    print("The PER is ", packetErrorRate)



def tensorflowtest():
    print(tf.version)


def main():
    PER = 10**(-6)
    print("PER ", PER)
    calculateBitErrorRate(PER)
    
    BER=10**(-6)
    calculatePacketErrorRate(BER)
    
    tensorflowtest();
    
    

if __name__ == "__main__":
   main()

