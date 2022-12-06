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
    isAttend = False
    isMet = False

    time = ""
    ms_time = ""
    isTimedigit = False
    value = 0
    str_value = ""
    target = ""
    n_target = 0
    value = 0

    while x < len(mot_action) and mot_action[x].lower() not in stopper:
        if mot_action[x] == '':
            x += 1
        print(f"Mot : {mot_action[x]}")
        if mot_action[x].lower() in cligno:
            print("Check Cligno")
            isCligno = True

        elif mot_action[x].lower() in allumer:
            isAllumer = True

        elif mot_action[x].lower() in extinction:
            print("Check extinction")
            isExtinction = True

        elif mot_action[x].lower() in article_defini:
            isArtDef = True

        elif mot_action[x].lower() in article_indefini:
            isArtIndef = True

        elif mot_action[x].lower() in adjectif_indefini:
            isAdjIndef = True

        elif mot_action[x].lower() in tout:
            isTout = True

        elif mot_action[x].lower() in attend:
            isAttend = True

        elif mot_action[x].lower() in met:
            isMet = True

        elif mot_action[x][0] in chiffre:
            str_value = mot_action[x]
            isTimedigit = False
            for i in range(len(str_value)):
                if str_value[i] not in chiffre and not isTimedigit:
                    time = str_value
                    for n in range(len(chiffre)):
                        time = time.replace(chiffre[n], '')
                    isTimedigit = True
            if isTimedigit:
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
                value = str_value
                for i in range(len(alphabet)):
                    value = value.replace(alphabet[i], "")
                value = formatage_txt(value)
                value = int(value)
            else:
                value = int(str_value)

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
            value = format_time(value, time)
            clearWrite(inoPath, f"digitalWrite({arduino[n_target].nom}, HIGH);\n"
                                f"delay({value});\n"
                                f"digitalWrite({arduino[n_target].nom}, LOW);\n"
                                f"delay({value});\n\n")
            increment_line(4)
    elif isAttend and isTime:
        value = format_time(value, time)
        clearWrite(inoPath, f"delay({value});\n\n")
        increment_line(1)

    elif isTargetLock and isMet:
        if arduino[n_target].type in digital_output:
            clearWrite(inoPath, f"digitalWrite({arduino[n_target].nom}, {value});")
            increment_line(1)
        elif arduino[n_target].type in analog_output:
            clearWrite(inoPath, f"analogWrite({arduino[n_target].nom}, {value});")
            increment_line(1)
    return x