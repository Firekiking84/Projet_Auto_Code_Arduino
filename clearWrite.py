def clearWrite(path, msg):
    file = open("current_line.txt", "r")
    current_line = file.read()
    file.close()
    file = open(path, "r")
    information = file.readlines()
    file.close()
    current_line = int(current_line)
    if current_line >= len(information):
        while len(information) <= current_line:
            information.append("\n")
            print(len(information))
    information[current_line] = msg
    file = open(path, "w")
    for x in range(len(information)):
        file.write(information[x])
    file.close()
    return
