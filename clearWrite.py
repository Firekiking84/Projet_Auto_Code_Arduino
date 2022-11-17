def clearWrite(path, msg):
    file = open("current_line.txt", "r")
    current_line = file.read()
    file.close()
    file = open(path, "r")
    information = file.readlines()
    file.close()
    information[int(current_line)] = msg
    file = open(path, "w")
    for x in range(len(information)):
        file.write(information[x])
    file.close()
    return
