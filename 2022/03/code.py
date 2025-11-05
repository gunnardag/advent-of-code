alphabet = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def a(input):
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            rug1 = l[0: int(len(l)/2)]
            rug2 = l[int(len(l)/2): len(l)]
            o =  []
            for i in rug1:  
                if i in rug2:
                    o.append(i)
            for i in set(o):
                sum = sum + alphabet.index(i)
        return sum


print('-------------A-------------')
print(f'test: {a("testinput")}')
print(f'real: {a("input")}')


def b(input):
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        group = []
        for l in lines:
            group.append(l)
            if len(group) != 3:
                pass
            else:
                tmp = group[0]+group[1]+group[2]
                tmp = tmp.replace('\n', '')
                for x in tmp:
                    if tmp.count(x) < 3:
                        tmp = tmp.replace(x, '')
                tmp = set(tmp)
                for x in tmp:
                    if x in group[0] and x in group[1] and x in group[2]:
                        print(f'found it: {x} with score {alphabet.index(x)}')
                        sum = sum + alphabet.index(x)
                group = []
    return sum

print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')
