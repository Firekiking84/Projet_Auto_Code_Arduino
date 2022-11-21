from liste import *
from clearWrite import clearWrite
from increment_line import increment_line
from name_finder import name_finder
from actionContent import actionContent


def condition(mot_action, x, inoPath, arduino):
    cndtn = ""
    cmp1 = ""
    cmp2 = ""
    cmp3 = ""

    if mot_action[x] in si:
        cndtn = "if"
        x += 1
    elif mot_action[x] == "sinon":
        if mot_action[x + 1] in si:
            cndtn = "else if"
            x += 2
        else:
            cndtn = "else"
            x += 1
    elif mot_action[x] in tant_que:
        cndtn = "while"
        x += 1
    elif mot_action[x] in tant:
        if mot_action[x + 1] == "que":
            cndtn = "while"
            x += 2

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
        cmp1 = f"{cmp1} "
        cmp2 = "== "
        cmp3 = "0"

    elif mot_action[x] in extinction:
        x += 1
        cmp1 = f"{cmp1} "
        cmp2 = "== "
        cmp3 = "1"

    find = False
    while x < len(mot_action) and not find and cmp3 == "":
        if mot_action[x].isdigit():
            cmp3 = mot_action[x]
            find = True
        else:
            cmp3 = name_finder(arduino, mot_action, x, inoPath)
            if cmp3 != "":
                find = True
        x += 1

    clearWrite(inoPath, f"{cndtn} ({cmp1}{cmp2}{cmp3}) {{\n\n}}\n\n")
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
