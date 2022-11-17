from input_read import input_read


def name_finder(arduino, mot_action, x, inoPath):
    n = 0
    cmp = ""
    while n < len(arduino):
        if arduino[n].nom.lower() == mot_action[x]:
            cmp = input_read(arduino, n, inoPath)
            n += 1
        else:
            n += 1
    return cmp