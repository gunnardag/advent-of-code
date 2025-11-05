def a_logic(elf1, elf2):
    return (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1])

def a(input):
    with open(input) as f:
        lines = f.readlines()
        c = 0
        for l in lines:
            p = l.split(',')
            e1 = p[0].split('-')
            elf1 = [int(e1[0]), int(e1[1])]
            e2 = p[1].split('-')
            elf2 = [int(e2[0]), int(e2[1])]
            
            if a_logic(elf1, elf2):
                print(f'ok: {l}')
                c = c + 1
            else:
                print(f'fails: {l}')
    return c

#print('-------------A-------------')
#print(f'test: {a("testinput")}')
#print(f'real: {a("input")}')


def b_logic(elf1, elf2):
    return elf1[1] < elf2[0] or elf1[0] > elf2[1]

def b(input):
    with open(input) as f:
        lines = f.readlines()
        c = 0
        for l in lines:
            p = l.split(',')
            e1 = p[0].split('-')
            elf1 = [int(e1[0]), int(e1[1])]
            e2 = p[1].split('-')
            elf2 = [int(e2[0]), int(e2[1])]
            
            if b_logic(elf1, elf2):
                print(f'ok: {l}')
            else:
                c = c + 1
                print(f'fails: {l}')
    return c

print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')
