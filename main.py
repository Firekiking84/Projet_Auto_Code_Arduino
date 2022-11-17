import os
from liste import *
from brain import Brain

path = os.getcwd()


def refresh_screen():
    for i in range(40):
        print("")


class Module:
    def __init__(self, nom, pin="N/A", type="digital"):
        self.nom = nom
        self.pin = pin
        self.type = type

arduino = []

file = open("current_line.txt", 'w')
file.write('0')
file.close()
current_line = 0

print('\033[93m')
print("Bienvenue dans l'Autocodeur Arduino !")
print('\033[91m')
print("        Appuie sur Entrée           ")
print('\033[0m')
reponse = str(input(""))

right = False
while not right:
    refresh_screen()
    reponse = str(input("Quel est le nom de ton projet ?\n--> ")).strip()

    if len(reponse) == 0:
        print("Il faut écrire quelque chose !")
    else:
        right= True
        reponse = formatage_txt(reponse)
        if not os.path.exists(f"{path}/Codes générés/{reponse}"):
            os.mkdir(f"{path}/Codes générés/{reponse}")
        file = open(f"{path}/Codes générés/{reponse}/{reponse}.ino", "w")
        file.close()
        inoPath = f"{path}/Codes générés/{reponse}/{reponse}.ino"

refresh_screen()
print(f"Nom final du fichier : {reponse}.ino")
right = False
while not right:
    reponse = str(input("Combien de modules sont branchés sur l'Arduino ? \n--> ")).strip()
    refresh_screen()
    nb_module = 0
    if reponse.isdigit():
        nb_module = int(reponse)
        right = True
    else:
        print("Ta réponse ne doit contenir que des chiffres !")

for i in range(nb_module):
    right = False
    while not right:
        if i == 0:
            reponse = str(input("Quel est le nom du premier module ?\n--> ")).strip()
        else:
            reponse = str(input(f"Quel est le nom du {i + 1}ème module ?\n--> ")).strip()
        refresh_screen()

        if len(reponse) == 0:
            print("Le module à besoin d'un nom !")
            right = False

        else:
            reponse = formatage_txt(reponse)
            arduino.append(Module(reponse))
            right = True

    arduino[len(arduino)-1].pin = str(input(f"Sur quel pin est branché {arduino[len(arduino)-1].nom}\n--> ")).strip()
    refresh_screen()

    print("En cas d'erreur, le pin peut être modifié directement sur le script")
    right = False
    while not right:
        print("Entre le numéro du choix qui te convient le mieux :")
        reponse = str(input(f"Paramètres basiques :           Paramètres préenregistré : \n\n"
                            f"1 : Sortie Digital              5 : Led\n"
                            f"2 : Entrée Digital              6 : Bouton poussoir\n"
                            f"3 : Sortie Analogique           7 : Moteur Pas à Pas\n"
                            f"4 : Entrée Analogique\n\n"
                            f"(Ajout de plus de types à venir !)--> "))
        right = True
        if reponse == '1':
            arduino[len(arduino)-1].type = "s_digital"
        elif reponse == '2':
            arduino[len(arduino) - 1].type = "e_digital"
        elif reponse == '3':
            arduino[len(arduino) - 1].type = "s_analog"
        elif reponse == '4':
            arduino[len(arduino) - 1].type = "e_analog"
        elif reponse == '5':
            arduino[len(arduino) - 1].type = "led"
        elif reponse == '6':
            arduino[len(arduino) - 1].type = "bp_pullup"
        elif reponse == '7':
            arduino[len(arduino) - 1].type = "p_motor"

        else:
            right = False
            refresh_screen()
            print("Il faut rentrer un chiffre correspondant à la liste !\n--> ")

define = ["s_digital", "e_digital", "s_analog", "e_analog", "led", "bp_pullup"]
file = open(f"{inoPath}", 'w')
for i in range(len(arduino)):

    # Définition des ports
    if arduino[i].type in define:
        file.write(f"#define {arduino[i].nom} {arduino[i].pin}\n")
        current_line += 1
    if arduino[i].type in analog_input or arduino[i].type in digital_input:
        file.write(f"int {arduino[i].nom}_value = 0;\n")
        current_line += 1

file.write("\nvoid setup()\n{\n")
current_line += 3
for i in range(len(arduino)):

    # void Setup

    if arduino[i].type == "s_digital" or arduino[i].type == "led":
        file.write(f"\tpinMode({arduino[i].nom}, OUTPUT);")
        current_line += 1
    elif arduino[i].type == "e_digital":
        file.write(f"\tpinMode({arduino[i].nom}, INPUT);")
        current_line += 1
    elif arduino[i].type == "bp_pullup":
        file.write(f"\tpinMode({arduino[i].nom}, INPUT_PULLUP);")
        current_line += 1
file.write("\n}\nvoid loop()\n{\n\n}")
current_line += 4
file.close()

reponse = str(input("Explique ce que tu comptes faire !\n -->")).strip()

file = open("current_line.txt", "w")
file.write(str(current_line))
file.close()
interpretation = reponse.lower().split(".")

Brain(interpretation, inoPath, arduino)