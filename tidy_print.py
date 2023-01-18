def printPicnic(itemDict,leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))

picnicItems = {'Paulaner': 4, 'beer': 5, 'water': 24}


print(printPicnic(picnicItems, 20, 6))