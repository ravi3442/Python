#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:35:59 2021

@author: raviravindran
"""
import random,sys, math

random.seed(0)

def rollDice():
    return random.choice([1,2,3,4,5,6])

def testRoll(n=10):
    result=''
    for i in range(n):
        result = result + str(rollDice())
    print(result)

def runsim(goal, numTrials, txt):
    total=0
    for i in range(numTrials):
        result=''
        for j in range(len(goal)):
            result +=str(rollDice())

        if result ==goal:
            total +=1
    print('Actual probability of ', txt, '=', round(1/(6**len(goal)),8))
    estProbability=round(total/numTrials,8)
    print('Total wins: ', total)
    #print('Estimated Probability of', txt, '=', round(estProbability,8))
    print('Estimated Probability of', txt, '=', estProbability)
    
    
def sameDate(numPeople, numSame):
    possibleDates = range(366)
    #possibleDates = 4*list(range(0,57))+[58]+4*list(range(59,366))+\
    #    4*list(range(59,366)) + 4*list(range(80,270))
    birthDays = [0]*366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthDays[birthDate]+=1
    return max(birthDays)>=numSame

def birthdayProb(numPeople, numSame, numTrials):
    numHits=0;
    for t in range(numTrials):
        if sameDate(numPeople, numSame):
            numHits+=1
    return numHits/numTrials

def runBirthDaySimuation():
    for numPeople in [10, 20, 40, 100]:
        print('For ', numPeople, 'est Prob. of shared birthday is ',
              birthdayProb(numPeople, 2, 10000))
    numerator=math.factorial(366)
    denom = (366**numPeople)*math.factorial(366-numPeople)
    print('Actual prob. of N =100 ', 1- (numerator/denom))
    

def main(argv):
    #runsim('11111', 1000, '11111')
   # testRoll(100)
   # runsim('11111', 500000, '11111')
   # print("People with same birthday", sameDate(100, 2))
    runBirthDaySimuation()
    
    



if __name__ == "__main__":
   main(sys.argv[1:])