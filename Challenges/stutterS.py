def stutter(str):
    str1 = str[:2]
    str1 += "... "
    str2 = ""
    for i in range(2):
        str2 += str1

    return str2+str