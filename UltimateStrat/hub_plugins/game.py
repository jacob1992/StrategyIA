#!/usr/bin/python

import Hub

# About Game
# ---Getter
@Hub.register_function
def getCurrentPlay():
    return Hub.black_board['game']['play']

@Hub.register_function
def getCurrentPlaySequence():
    return Hub.black_board['game']['sequence']

# ---Setter
@Hub.register_function
def setPlay(play):
    Hub.black_board['game']['play'] = play

# Special stuff
@Hub.register_function
def initPlaySequence():
    Hub.black_board['game']['sequence'] = 0

@Hub.register_function
def incPlaySequence():
    Hub.black_board['game']['sequence'] += 1

@Hub.register_function
def getPrevPlayerPosition(i):
    return Hub.black_board['friend'][str(i - 1)]['position']
