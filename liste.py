def formatage_txt(txt):
    SpeCharac = "&(-)=][°/\|`#~!?,;.:§*$"
    for x in range(len(SpeCharac)):
        txt = txt.replace(SpeCharac[x], "")
    SpeA = "àäâ"
    for x in range(len(SpeA)):
        txt = txt.replace(SpeA[x], "a")
    SpeE = "éèëê"
    for x in range(len(SpeE)):
        txt = txt.replace(SpeE[x], "e")
    txt = txt.replace(' ', '_')
    txt = txt.replace("'", '_')
    return txt


"""Vocabulaire"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
si = ["if", "si", "quand"]
tant_que = ["while", "tantque"]
tant = ["tant", "tandis"]
cligno = ["clignoter", "clignoté", "clignote"]
allumer = ["s'allume", "allume", "allumer", "allumé", "s'allumer", "s'allumé", "allumée", "s'allumée", "activé",
           "active", "activer"]
extinction = ["s'eteind", "s'eteint", "s'éteind", "s'éteint", "eteind", "eteint", "éteint", "éteind", "éteins",
              "eteins"]
article_defini = ["les", "la", "le"]
article_indefini = ["un", "une", "des"]
adjectif_indefini = ["Aucun", "autre", "certain", "chaque", "différents", "divers", "l'un", "l'autre", "maint", "même",
                     "nul", "plusieurs", "quel", "quelconque", "quelque", "tel", "tout"]
chiffre = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
tout = ["tous", "tout", "toutes", "toute"]
inferieur = ["inferieur", "sous", "inférieur"]
egal = ["egal", "egale", "égale", "égal"]
superieur = ["superieur", "au-dessus", "supérieur"]
a = ["a", "à"]
alors = ["alors", "Alors"]
ensuite = ["ensuite", "après", "apres", "puis"]
stopper = [".", "et", ","]

"""Time Unit"""

time_unit = ["h", "heure", "heures", "min","minutes", "minute",  "s", "seconde", "secondes", "ms", "millisecondes",
             "milliseconde"]

"""Type"""

analog_input = ["e_analog"]
digital_input = ["bp_pullup", "e_digital"]
digital_output = ["s_digital", "led"]
