def format_time(time_value, time_unit):
    if time_unit == "h":
        time_value = time_value * 3.6 * pow(10, 6)
    elif time_unit == "min":
        time_value = time_value * 6000
    elif time_unit == "s":
        time_value = time_value * 1000
    elif time_unit == "ms":
        time_value = time_value
    return time_value