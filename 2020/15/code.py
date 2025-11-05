from pprint import pprint
with open('input') as f:
    lines = f.readlines()
    j = 0
    while j < len(lines):
        if 'acc' in lines[j]:
            j = j + 1
        else:
            tmp = lines.copy()
            if 'nop' in tmp[j]:
                tmp[j] = tmp[j].replace('nop', 'jmp')
            elif 'jmp' in tmp[j]:
                tmp[j] = tmp[j].replace('jmp', 'nop')
            acc = 0
            i = 0
            done = []
            while i < len(tmp):
                if i in done:
                    break
                done.append(i)
                command, vals = tmp[i].split(' ')
                val = int(vals)
                if command == 'nop':
                    i = i+1
                elif command == 'acc':
                    acc = acc + val
                    i = i+1
                elif command == 'jmp':
                    i = i + val
            if i == len(lines):
                print(acc)
            j = j + 1