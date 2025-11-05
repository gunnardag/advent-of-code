with open('input') as f:
    lines = f.readlines()
    index = 0
    trees = 0

    for i in lines:
        i = i.rstrip()
        if i[(index*3) % len(i)] == '#':
            print("TREE")
            trees = trees +1
        else:
            print("CLEAR")
        index = index + 1

    print(trees)
