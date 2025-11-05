def a(input):
    with open('input') as f:
        lines = f.readlines()
        maxsum = 0
        sum = 0
        for l in lines:
            if l == "\n":
                if sum > maxsum:
                    maxsum = sum
                sum = 0
            else:
                sum = sum + int(l)
        if sum > maxsum:
            maxsum = sum
        print(maxsum)

a('testinput') # 24000
a('input') # 71506

def b(input):
    with open(input) as f:
        lines = f.readlines()
        sums = []
        sum = 0
        for l in lines:
            if l == "\n":
                sums.append(sum)
                sum = 0
            else:
                sum = sum + int(l)
        sums.append(sum)
        total = 0
        for i in range(0,3):
            total = total + max(sums)
            sums.remove(max(sums))
        print(total)
print('test:')
b('testinput') # 45000
print('real:')
b('input') # 209603