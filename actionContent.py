from liste import *
from increment_line import increment_line
from clearWrite import clearWrite
from format_time import format_time


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
    isTargetLock = False

    time = ""
    ms_time = ""
    time_value = 0
    str_value = ""
    target = ""
    n_target = 0
    value = 0

    while x < len(mot_action) and mot_action[x].lower() not in stopper:
        print(f"len : {len(mot_action)}\n x: {x}\n\n")
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
            str_value = mot_action[x]
            n = 0
            for i in range(len(str_value)):
                if str_value[i] not in chiffre:
                    time[n] = str_value[i]
                    n += 1
            if n != 0:
                for i in range(len(time_unit)):
                    if time == time_unit[i]:
                        isTime = True
                        if i < 3:
                            time = "h"

                        elif 3 <= i < 6:
                            time = "min"

                        elif 6 <= i < 9:
                            time = "s"

                        elif i >= 9:
                            time = "ms"

                        else:
                            time = ""
                            isTime = False
                for x in range(len(alphabet)):
                    time_value = str_value.replace(alphabet[x], "")
                    time_value = formatage_txt(time_value)
                    time_value = int(time_value)
            else:
                time_value = int(str_value)

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

        else:
            for t in range(len(arduino)):
                if arduino[t].nom.lower() == mot_action[x].lower():
                    target = arduino[t].nom
                    n_target = t
            if target != "":
                isTargetLock = True
        x += 1

    if isTargetLock and isAllumer:
        if arduino[n_target].type in digital_output:
            clearWrite(inoPath, f"digitalWrite({arduino[n_target].nom}, HIGH);\n\n")
            increment_line(1)

    elif isTargetLock and isExtinction:
        if arduino[n_target].type in digital_output:
            clearWrite(inoPath, f"digitalWrite({arduino[n_target].nom}, LOW);\n\n")
            increment_line(1)

    elif isTargetLock and isCligno and isTime:
        if arduino[n_target].type in digital_output:
            time_value = format_time(time_value, time)
            clearWrite(inoPath, f"digitalWrite({arduino[n_target].nom}, HIGH);\n"
                                f"delay({time_value});\n"
                                f"digitalWrite({arduino[n_target].nom}, LOW);\n"
                                f"delay({time_value});\n\n")
            increment_line(4)
    return x