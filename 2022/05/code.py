def a(input):
    with open(input) as f:
        lines = f.readlines()
        count = int(len(lines[0])/4)
        stacks = []
        for x in range(0, count):
            stacks.append([])
        done = False
        for l in lines:
            if not done:
                if len(l) == 1:
                    for i in range(0,count):
                        stacks[i].reverse()
                    done = True
                else:
                    for i in range (0, count):
                        crate = l[(i*4)+1]
                        if crate != ' ' and not crate.isnumeric():
                            stacks[i].append(crate)
            else:
                a = l.strip().split(' ')
                for i in range(0, int(a[1])):
                    stacks[int(a[5])-1].append(stacks[int(a[3])-1].pop())

        answer = ''
        for i in stacks:
            answer = answer+i.pop()
        return answer





print('-------------A-------------')
print(f'test: {a("testinput")}')
print(f'real: {a("input")}')



def b(input):
    with open(input) as f:
        lines = f.readlines()
        count = int(len(lines[0])/4)
        stacks = []
        tmp = []
        for x in range(0, count):
            stacks.append([])
        done = False
        for l in lines:
            if not done:
                if len(l) == 1:
                    for i in range(0,count):
                        stacks[i].reverse()
                    done = True
                else:
                    for i in range (0, count):
                        crate = l[(i*4)+1]
                        if crate != ' ' and not crate.isnumeric():
                            stacks[i].append(crate)
            else:
                a = l.strip().split(' ')
                for i in range(0, int(a[1])):
                    tmp.append(stacks[int(a[3])-1].pop())
                for i in range(0, int(a[1])):
                    stacks[int(a[5])-1].append(tmp.pop())

        answer = ''
        for i in stacks:
            answer = answer+i.pop()
        return answer

print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')
