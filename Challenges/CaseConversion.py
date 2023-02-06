def func(s):
    str = ""
    for i in s:
        if i.islower():
           str += i.capitalize()
        else:
            str += i.lower()
    return str
