#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:21:28 2022

@author: raviravindran
"""

class HalvingGame(object):
    def __init__(self, N):
        self.N=N
    
    
    def startState(self):
        return (+1, self.N)

    def isEnd(self, state):
        player, number = state
        return number== 0
    
    def utility (self, state):
        player, number = state
        assert number ==0
        #print("Player: ", player)
        return player*float('inf')
    
    def actions (self, state):
        return ['-', '/']
    
    def player(sel, state):
        player, number = state
        return player
    
    def succ(self, state, action):
        player, number = state
        if action == '-':
            return (-player, number-1)
        if action == '/':
            return (-player, number//2)
        
    
def humanPolicy(game, state):
    while True:
        action =  input('Input Action ')
        if action in  game.actions(state):
            return action


def miniMaxPolicy(game, state):
    def recurse(state):
        if game.isEnd(state):
            return (game.utility(state), 'none')
        choices = [(recurse(game.succ(state, action))[0],action )for action in game.actions(state)]
        print(choices)
        if game.player(state)==+1:
            return max(choices)
        elif game.player(state)==-1:
            return min(choices)
        value, action = recurse(state)
        print('minimax says action= {}, value ={}'.format(action, value))
        return action

        

policies = {+1:humanPolicy, -1:miniMaxPolicy}
print ("Input the Number for the halving game")
N=input()
game= HalvingGame(int(N))
state = game.startState()

while not game.isEnd(state):
    print("Player to Play and State ", state)
    player = game.player(state)
    policy= policies[player]
    action = policy(game, state)
    state = game.succ(state, action)


player = game.player(state)

if player == 1:
    print('Player +1 won with utility = {}'.format(game.utility(state)))
elif player == -1:
    print('Player -1 won with utility = {}'.format(game.utility(state)))





    