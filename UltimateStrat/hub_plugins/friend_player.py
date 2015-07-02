#!/usr/bin/python

import Hub

# About Friend player
# ---Getter
@Hub.register_function
def getPlayerTarget(i):
    return Hub.black_board['friend'][str(i)]['target']

@Hub.register_function
def getPlayerGoal(i):
    return Hub.black_board['friend'][str(i)]['goal']

@Hub.register_function
def getPlayerSkill(i):
    return Hub.black_board['friend'][str(i)]['skill']

@Hub.register_function
def getPlayerTactic(i):
    return Hub.black_board['friend'][str(i)]['tactic']

@Hub.register_function
def getPlayerPosition(i):
    return Hub.black_board['friend'][str(i)]['position']

@Hub.register_function
def getPlayerPose(i):
    return Hub.black_board['friend'][str(i)]['pose']

@Hub.register_function
def getPlayerOrientation(i):
    return Hub.black_board['friend'][str(i)]['orientation']

@Hub.register_function
def getPlayerKickState(i):
    return Hub.black_board['friend'][str(i)]['kick']

@Hub.register_function
def getCountPlayer():
    return Hub.black_board['friend']['count']

@Hub.register_function
def getPlayerNextPose(i):
    return Hub.black_board['friend'][str(i)]['next_pose']

# ---Setter
@Hub.register_function
def setPlayerSkillTargetGoal(i, action):
    Hub.black_board['friend'][str(i)]['skill'] = action['skill']
    Hub.black_board['friend'][str(i)]['target'] = action['target']
    Hub.black_board['friend'][str(i)]['goal'] = action['goal']

@Hub.register_function
def setPlayerTactic(i, tactic):
    Hub.black_board['friend'][str(i)]['tactic'] = tactic

@Hub.register_function
def setPlayerNextPose(i, next_pose):
    Hub.black_board['friend'][str(i)]['next_pose'] = next_pose

