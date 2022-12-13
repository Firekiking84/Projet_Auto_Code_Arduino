from liste import *
from increment_line import increment_line


def isCondition(mot_action, x):
    print(f"IsCondition : {mot_action[x]}, {mot_action[x + 1]} ?")
    isACondition = False
    if mot_action[x] in ensuite:
        increment_line(2)
        print("Skip Check")
        x += 1
    if mot_action[x] in si:
        isACondition = True
    elif mot_action[x] == "sinon":
        isACondition = True
    elif mot_action[x] in tant_que:
        isACondition = True
    elif mot_action[x] in tant:
        if mot_action[x + 1]:
            isACondition = True
    if isACondition:
        print("Condition Check !")
    return isACondition
