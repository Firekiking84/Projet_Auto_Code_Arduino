from liste import *


def Brain(reponse, inoPath, arduino):
    i = 0
    while i <= len(reponse):
        mot_action = reponse[i].strip(" ")
        x = 0
        while x <= len(mot_action):
            if mot_action[x] in si:
                x += 1
                n = 0
                cmp1 = ""
                cmp2 = ""
                cmp3 = ""
                while n <= len(arduino):
                    if arduino.nom == mot_action[x]:
                        cmp1 == arduino.nom
                    else:
                        n += 1
                if cmp1 == "":
                    print("Erreur ! Pas de nom dans la condition.")
                    return
                x += 1
                if mot_action[x] == "est":
                    x += 1

                if mot_action[x] == "moins" and mot_action[x + 1] == "que":
                    x += 2
                    cmp2 = inf_ou_egal(mot_action, x)

                elif mot_action[x] in inferieur:
                    x += 1
                    cmp2 = inf_ou_egal(mot_action, x)

                elif mot_action[x] == "plus" and mot_action[x+1] == "que":
                    x += 2
                    cmp2 = sup_ou_egal(mot_action, x)

                elif mot_action[x] in superieur:
                    x += 1
                    cmp2 = sup_ou_egal(mot_action, x)

                elif mot_action[x] in egal:
                    x += 1
                    cmp2 = "=="

                elif mot_action[x] in allumer:
                    x += 1
                    cmp1 == f"digitalRead({cmp1}) "
                    cmp2 == "== "
                    cmp3 == "HIGH"

                elif mot_action[x] in extinction:
                    x += 1
                    cmp1 == f"digitalRead({cmp1}) "
                    cmp2 == "== "
                    cmp3 == "LOW"

                else:
                    while x <= len(mot_action):
                        if mot_action[x].isdigit():
                            cmp3 = mot_action[x]

                file = open(f"{inoPath}", "a")
                file.write(f"if ({cmp1}{cmp2}{cmp3}) {{")


def inf_ou_egal(mot_action, x):
    if mot_action[x + 1] == "ou" and mot_action[x + 2] in egal:
        x += 3
        cmp2 = "<="
    else:
        cmp2 = "<"
    return cmp2


def sup_ou_egal(mot_action, x):
    if mot_action[x + 1] == "ou" and mot_action[x + 2] in egal:
        x += 3
        cmp2 = "<="
    else:
        cmp2 = "<"
    return cmp2