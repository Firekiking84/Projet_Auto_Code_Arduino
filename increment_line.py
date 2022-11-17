def increment_line(add):
    file = open("current_line.txt", "r")
    info = file.read()
    file.close()
    info = int(info) + add
    file = open("current_line.txt", "w")
    file.write(str(info))
    return int(info)