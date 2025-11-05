def a(input):
    with open(input) as f:
        register = 1
        cycle = 1
        signals = []
        lines = f.readlines()
        for l in lines:
            if cycle in [20, 60, 100, 140, 180, 220]:
                signals.append(register * cycle)
            if l.strip() == 'noop':
                cycle = cycle + 1
            else:
                cycle = cycle + 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    signals.append(register * cycle)
                cycle = cycle + 1
                register = register + int(l.split(' ')[1])

    print(cycle)
    print(register)
    print(signals)
    from functools import reduce
    return reduce((lambda x, y: x + y), signals)
    
#print('-------------A-------------')
#print(f'test: {a("testinput")}')
#print(f'real: {a("input")}')

def b(input):
    with open(input) as f:
        register = 0
        cycle = 0
        lines = f.readlines()
        stuff = ''
        for l in lines:
            print(f"Start cycle {cycle}, register {register}")
            if cycle%40 in [register,register+1,register+2]:
                stuff = stuff + '#'
            else:
                stuff = stuff + '.'
            if l.strip() == 'noop':
                cycle = cycle + 1
            else:
                cycle = cycle + 1
                print(f"During cycle {cycle}, register {register}")
                if cycle%40 in [register,register+1,register+2]:
                    stuff = stuff + '#'
                else:
                    stuff = stuff + '.'
                cycle = cycle + 1
                register = register + int(l.split(' ')[1])

    for i in range(0, 6):
        print(stuff[i*40:(i*40)+40])
print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')