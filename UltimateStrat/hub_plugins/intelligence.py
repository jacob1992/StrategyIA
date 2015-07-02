#!/usr/bin/python

import Hub

# State machine
# TODO implement getNextState
@Hub.register_function
def getNextState():
    return 'debug'

# TODO implement getNextPlay
@Hub.register_function
def getNextPlay(state):
    return 'pQueueLeuLeu'
