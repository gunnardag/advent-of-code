
def a(input):
    with open(input) as f:
        lines = f.readlines()
        b = ['root']
        c = {}
        sum = 0
        for l in lines:
            l = l.strip()
            cmd = l.split(' ')
            if cmd[0].isnumeric():
                o = []
                for x in b:
                    o.append(x)
                    if '.'.join(o) in c:
                        c['.'.join(o)] = c['.'.join(o)] + int(cmd[0])
                    else:
                        c['.'.join(o)] = int(cmd[0])
                
            elif cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] != '/':
                if cmd[2] == '..':
                    b.pop()
                else:
                    b.append(cmd[2])
        for x in c:
            if c[x] < 100000:
                sum = sum + c[x]
        print(c)
        print(sum)


#print('-------------A-------------')
#print(f'test: {a("testinput")}')
#print(f'real: {a("input")}')


def b(input):
    with open(input) as f:
        lines = f.readlines()
        b = ['root']
        c = {}
        sum = 0
        for l in lines:
            l = l.strip()
            cmd = l.split(' ')
            if cmd[0].isnumeric():
                o = []
                for x in b:
                    o.append(x)
                    if '.'.join(o) in c:
                        c['.'.join(o)] = c['.'.join(o)] + int(cmd[0])
                    else:
                        c['.'.join(o)] = int(cmd[0])
                
            elif cmd[0] == '$' and cmd[1] == 'cd' and cmd[2] != '/':
                if cmd[2] == '..':
                    b.pop()
                else:
                    b.append(cmd[2])
        for x in c:
            if c[x] < 100000:
                sum = sum + c[x]
        print(c)
        d = c['root']- 40000000
        print(d)
        e = {}
        for x in c:
            if c[x] >= d:
                e[x] = c[x]
        print(e)
        print(min(e, key=e.get))
        print(e[min(e, key=e.get)])

print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')