with open('input') as f:
    lines = f.readlines()
    line = ''
    y = 0
    for i in lines:
        i = i.rstrip()
        if line == '':
            line = i
        else:
            line = f'{line}{i}'
        if i == '':
            y = y + len(set(line.rstrip()))
            line = ''
    print(y)