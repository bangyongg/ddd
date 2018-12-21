

def encrypt(stringarray):
    stringarray = stringarray.rstrip()

    if len(stringarray) > 100:
        return "your text too long"

    stringarray = stringarray.rstrip()
    midlist = list(stringarray)
    templist = list()

    for x in range(0, stringarray.__len__(), 2):
        templist.append(midlist[x])

    for x in range(1, stringarray.__len__(), 2):
        templist.append(midlist[x])

    resultstr = ''.join(templist)

    return resultstr