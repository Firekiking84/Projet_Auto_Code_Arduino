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


si = ["if", "si", "quand"]
tant_que = ["while", "tantque"]
tant = ["tant", "tandis"]
cligno = ["clignoter", "clignoté", "clignote"]
allumer = ["s'allume", "allume", "allumer", "allumé", "s'allumer", "s'allumé", "allumée", "s'allumée"]
extinction = ["s'eteind", "s'eteint", "s'éteind", "s'éteint", "eteind", "eteint", "éteint", "éteind"]
article_defini = ["les", "la", "le"]
article_indefini = ["un", "une", "des"]
adjectif_indefini = ["Aucun", "autre", "certain", "chaque", "différents", "divers", "l'un", "l'autre", "maint", "même",
                     "nul", "plusieurs", "quel", "quelconque", "quelque", "tel", "tout"]
chiffre = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
time_unit = ["heure", "heures", "minutes", "minute", "seconde", "secondes", "millisecondes", "milliseconde"]
tout = ["tous", "tout", "toutes", "toute"]
inferieur = ["inferieur", "sous"]
egal = ["egal", "egale"]
superieur = ["superieur", "au-dessus"]