from liste import *
from clearWrite import clearWrite
from increment_line import increment_line
from name_finder import name_finder
from actionContent import actionContent


def IfCondition(mot_action, x, inoPath, arduino):
    x += 1
    cmp2 = ""
    cmp3 = ""

    cmp1 = name_finder(arduino, mot_action, x, inoPath)

    if cmp1 == "":
        print("Erreur ! Pas de nom dans la condition.")
        return
    x += 1

    if mot_action[x] == "est":
        x += 1
        if mot_action[x] in a:
            cmp2 = " == "
            x += 1

    elif mot_action[x] in egal:
        x += 1
        cmp2 = " == "

    if mot_action[x] == "moins" and mot_action[x + 1] == "que":
        x += 2
        cmp2 = inf_ou_egal(mot_action, x)

    elif mot_action[x] in inferieur:
        x += 1
        cmp2 = inf_ou_egal(mot_action, x)

    elif mot_action[x] == "plus" and mot_action[x + 1] == "que":
        x += 2
        cmp2 = sup_ou_egal(mot_action, x)

    elif mot_action[x] in superieur:
        x += 1
        cmp2 = sup_ou_egal(mot_action, x)

    if mot_action[x] in allumer:
        x += 1
        cmp1 = f"digitalRead({cmp1}) "
        cmp2 = "== "
        cmp3 = "HIGH"

    elif mot_action[x] in extinction:
        x += 1
        cmp1 = f"digitalRead({cmp1}) "
        cmp2 = "== "
        cmp3 = "LOW"

    find = False
    while x < len(mot_action) and not find:
        if mot_action[x].isdigit():
            cmp3 = mot_action[x]
            find = True
        else:
            cmp3 = name_finder(arduino, mot_action, x, inoPath)
            if cmp3 != "":
                find = True
        x += 1

    clearWrite(inoPath, f"if ({cmp1}{cmp2}{cmp3}) {{\n\n}}\n\n")
    increment_line(1)

    if x < len(mot_action):
        x = actionContent(mot_action, x, inoPath, arduino)
    return x


def inf_ou_egal(mot_action, x):
    if mot_action[x] == "ou" and mot_action[x + 1] in egal:
        x += 2
        cmp2 = " <= "
    else:
        cmp2 = " < "
    return cmp2


def sup_ou_egal(mot_action, x):
    if mot_action[x] == "ou" and mot_action[x + 1] in egal:
        x += 2
        cmp2 = " >= "
    else:
        cmp2 = " > "
    return cmp2
