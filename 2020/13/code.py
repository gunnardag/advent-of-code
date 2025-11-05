from pprint import pprint
with open('input') as f:
    lines = f.readlines()
    map = {}
    for line in lines:
        line = line.rstrip()
        o = line.split(" contain ")
        if not 'no other bag' in o[1]:
            map[o[0][0:-1]] = o[1]


    print(len(map))
    # pprint(map)

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