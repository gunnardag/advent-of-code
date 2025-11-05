with open('input') as f:
    lines = f.readlines()
    for l in lines:
        for k in lines:
            if int(l) + int(k) == 2020:
                print(f'{l} + {k} = 2020')
                print(f'{l} * {k} = {int(l) * int(k)}')
