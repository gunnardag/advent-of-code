with open('input') as f:
    lines = f.readlines()
    ints = []
    for i in lines:
        ints.append(int(i))

    for l in ints:
        for k in ints:
            for j in ints:
                if l + k + j == 2020:
                    print(f'{l} + {k} + {j} = 2020')
                    print(f'{l} * {k} * {j} = {l*j*k}')
