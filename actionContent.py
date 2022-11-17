from liste import *
from increment_line import increment_line


def actionContent(mot_action, x, inoPath, arduino):
    if mot_action[x] in ensuite:
        increment_line(2)

    elif mot_action[x] in alors:
        x += 1

    isCligno = False
    isAllumer = False
    isExtinction = False
    isTime = False
    isArtDef = False
    isArtIndef = False
    isAdjIndef = False
    isTout = False

    time = ""
    value = 0

    while mot_action[x].lower() not in stopper or x >= len(mot_action):
        if mot_action[x].lower() in cligno:
            isCligno = True

        elif mot_action[x].lower() in allumer:
            isAllumer = True

        elif mot_action[x].lower() in extinction:
            isExtinction = True

        elif mot_action[x].lower() in article_defini:
            isArtDef = True

        elif mot_action[x].lower() in article_indefini:
            isArtIndef = True

        elif mot_action[x].lower() in adjectif_indefini:
            isAdjIndef = True

        elif mot_action[x].lower() in tout:
            isTout = True

        elif mot_action[x][0] in chiffre:


        elif mot_action[x].lower() in time_unit:
            for i in range(len(time_unit)):
                if mot_action[x].lower() == time_unit[i]:
                    if i < 3:
                        time = "h"

                    elif 3 <= i < 6:
                        time = "min"

                    elif 6 <= i < 9:
                        time = "s"

                    elif i >= 9:
                        time = "ms"
            isTime = True


        x += 1