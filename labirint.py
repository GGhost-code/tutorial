def labyrinth(lab):
    i, j = -1, -1
    way = ""

    for s in range(len(lab)):
        for t in range(len(lab[0])):
            if lab[s][t] == 'i':
                i, j = s, t

    while True:
        if lab[i][j] == 'i':
            lab[i][j] = '.'

        if i == len(lab[0]) - 1 or i == 0 or j == 0 or j == len(lab) - 1:
            break

        if lab[i][j + 1] != '#' and lab[i][j + 1] != '.':
            j += 1
            way += "R"
            print("Right", i, j)
            if lab[i][j] == '.':
                break

        elif lab[i + 1][j] != '#' and lab[i + 1][j] != '.':
            i += 1
            way += "D"
            print("Down", i, j)
            if lab[i][j] == '.':
                break

        elif lab[i][j - 1] != '#' and lab[i][j - 1] != '.':
            j -= 1
            way += "L"
            print("Left", i, j, way)
            if lab[i][j] == '.':
                break

        elif lab[i - 1][j] != '#' and lab[i - 1][j] != '.':
            i -= 1
            way += "U"
            print("Up", i, j)
            if lab[i][j] == '.':
                break

        for k in lab:
            print(k)

    return way

l = [['#', '#', '#', '#'],
     ['#', ' ', ' ', ' '],
     ['#', ' ', 'i', '#'],
     ['#', '#', '#', '#'],]

print(labyrinth(l))