def reverse():
    a = input()
    return reverse() + a if a != "0" else ""

def idiot_reverse():
    a = input()
    if int(a) != 0:
        idiot_reverse()
    else:
        return 0
    print(a if a != "0" else "")
idiot_reverse()