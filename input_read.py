from clearWrite import clearWrite
from liste import *
from increment_line import increment_line


def input_read(arduino, n, inoPath):
    if arduino[n].type in analog_input:
        clearWrite(inoPath, f"{arduino[n].nom}_value = analogRead({arduino[n].nom});\n\n")
        increment_line(1)
        cmp = f"{arduino[n].nom}_value"
    elif arduino[n].type in digital_input:
        clearWrite(inoPath, f"{arduino[n].nom}_value = digitalRead({arduino[n].nom});\n\n")
        increment_line(1)
        cmp = f"{arduino[n].nom}_value"
    else:
        cmp = arduino[n].nom
    return cmp