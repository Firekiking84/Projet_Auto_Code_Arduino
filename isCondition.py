from liste import *


def isCondition(mot_action, x):
    isACondition = False
    if mot_action[x] in si:
        isACondition = True
    elif mot_action[x] == "sinon":
        isACondition = True
    elif mot_action[x] in tant_que:
        isACondition = True
    elif mot_action[x] in tant:
        if mot_action[x + 1]:
            isACondition = True
    return isACondition