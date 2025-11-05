def check(min, max, letter, word):
    e = 0
    if word[min-1] == letter:
        e = e + 1
    if word[max-1] == letter:
        e = e + 1
    return e == 1

with open('input') as f:
    lines = f.readlines()
    e = 0
    for i in lines:
        s = i.split(' ')
        min = int(s[0].split('-')[0])
        max = int(s[0].split('-')[1])
        letter = s[1][0:1]
        word = s[2]
        if check(min, max, letter, word):
            e = e + 1
            print(i)
    print(e)