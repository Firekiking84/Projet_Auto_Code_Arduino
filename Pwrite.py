def clearWrite(path, msg):
    file = open(path, "r")
    information = file.readlines()
    file.close()
    for i in range(len(information)):
        if information[i] == "\n":
            information[i] = msg
            file = open(path, "w")
            for x in range(len(information)):
                file.write(information[x])
            file.close()
            return
