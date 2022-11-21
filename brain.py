from condition import condition
from liste import *
from actionContent import actionContent
from isCondition import isCondition


def Brain(reponse, inoPath, arduino):
    i = 0
    mot_action = []
    while i < len(reponse):
        mot_action = reponse[i].split(" ")
        for n in range(len(mot_action)):
            mot_action[n] = mot_action[n].replace(",", " ,")
        mot_action = ' '.join(mot_action)
        mot_action = mot_action.split(' ')
        x = 0
        while x < len(mot_action):
            if isCondition(mot_action, x):
                x = condition(mot_action, x, inoPath, arduino)

            else:
                x = actionContent(mot_action, x, inoPath, arduino)
            x += 1
        i += 1