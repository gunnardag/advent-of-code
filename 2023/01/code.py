import re

def a(input):
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            l = ''.join(filter(str.isdigit, l))
            intstr = f'{l[0]}{l[len(l)-1]}'
            n = int(intstr)
            sum = sum + n
        print(sum)

# print('test:')
# a('testinput') # 142
# print('real:')
# a('input') # 56049

def b(input):
    numbers = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            m = {}
            for n in numbers.keys():
                for o in [m.start() for m in re.finditer(f'(?={n})', l)]:
                    m[o] = numbers[n]

            a = sorted(m)
            intstr = f'{m[a[0]]}{m[a[len(m)-1]]}'
            n = int(intstr)
            sum = sum + n
        print(sum)
print('test:')
b('testinput') # 281
print('real:')
b('input') # 209603
