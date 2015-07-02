#!/usr/bin/python

import Hub

# About Ball
# ---Getter
@Hub.register_function
def getBallPosition():
    return Hub.black_board['ball']['position']
