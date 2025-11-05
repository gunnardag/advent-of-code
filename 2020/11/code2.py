with open('input') as f:
    lines = f.readlines()
    y = 0
    sets = []
    for i in lines:
        i = i.rstrip()
        if i != '':
            sets.append(set(i))
        elif i == '':
            print(sets)
            ss = sets[0]
            for s in sets[1:]:
                ss = ss.intersection(s)
            y = y + len(ss)
            sets = []

    print(y)