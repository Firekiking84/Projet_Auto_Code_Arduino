from IfCondition import IfCondition
from liste import *
from actionContent import actionContent


def Brain(reponse, inoPath, arduino):
    i = 0
    mot_action = []
    while i < len(reponse):
        mot_action = reponse[i].split(" ")
        x = 0
        while x < len(mot_action):
            if mot_action[x] in si:
                x = IfCondition(mot_action, x, inoPath, arduino)

            else:
                x = actionContent(mot_action, x, inoPath, arduino)
            x += 1
        i += 1