from pprint import pprint
with open('input') as f:
    lines = f.readlines()
    map = {}
    map2 = {}
    for line in lines:
        line = line.rstrip()
        o = line.split(" contain ")
        if 'no other' in o[1]:
            map2[o[0][0:-1]] = 1
        else:
            map[o[0][0:-1]] = o[1].split(', ')
    pprint(map)
    pprint(map2)
while len(map) > 0:
    for i in map:
        c = 0
        sum = 1
        for o in map[i]:
            for d in map2:
                if d in o:
                    c = c + 1
                    sum = sum + int(o[0]) * map2[d]
        if c == len(map[i]):
            print(f"wow, {i} contains {sum} bags")
            map2[i] = sum

    for i in map2:
        if i in map:
            map.pop(i)
pprint(map)
pprint(map2)
    
'''
    baglist = set(['shiny gold bag'])
    l = 1
    while(True):
        for i in map:
            m = map[i].replace('bag.', 'bags.')
            if any(bag in m for bag in baglist):
                baglist.add(i)
        if len(baglist) == l:
            break
        l = len(baglist)
    baglist.remove('shiny gold bag')
    print(baglist)
    print(len(baglist))
    '''


{
    'dark blue bag': ['2 dark violet bags.'],
    'dark green bag': ['2 dark blue bags.'],
    'dark orange bag': ['2 dark yellow bags.'],
    'dark red bag': ['2 dark orange bags.'],
    'dark violet bag': ['no other bags.'],
    'dark yellow bag': ['2 dark green bags.'],
    'shiny gold bag': ['2 dark red bags.']
}

{
    'dark blue bag': ['2 dark violet bags.'],
    'dark green bag': ['2 dark blue bags.'],
    'dark orange bag': ['2 dark yellow bags.'],
    'dark red bag': ['2 dark orange bags.'],
    'dark violet bag': 1,
    'dark yellow bag': ['2 dark green bags.'],
    'shiny gold bag': ['2 dark red bags.']
}

{
    'dark blue bag': (2 * 1) + 1,
    'dark green bag': (2 * ((2 * 1) + 1)) + 1,
    'dark orange bag': (2 * (2 * (2 * (2 * 1) + 1) + 1) + 1) + 1,
    'dark red bag': (2 * (2 * (2 * (2 * (2 * 1) + 1) + 1) + 1) + 1) + 1,
    'dark violet bag': 1,
    'dark yellow bag': (2 * (2 * (2 * 1) + 1) + 1) + 1,
    'shiny gold bag': (2 * ((2 * ((2 * ((2 * ((2 * ((2 * 1) + 1)) + 1)) + 1)) + 1)) + 1)) + 1
}

{
    'dark blue bag': 3,
    'dark green bag': "2 * 3 + 1 = 7",
    'dark orange bag': "2 * 15 + 1 = 31",
    'dark red bag': "2 * 31 + 1 = 63",
    'dark violet bag': 1,
    'dark yellow bag': "2 * 7 + 1 = 15",
    'shiny gold bag': "2 * 63 + 1 = 127",
}