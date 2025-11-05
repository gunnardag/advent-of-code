

with open('input') as f:
    lines = f.readlines()

    def check_trees(right, down):
        index = 0
        trees = 0
        for i in lines:
            if down == 2:
                if index % down == 1:
                    index = index + 1
                else:
                    i = i.rstrip()
                    if i[(int(index / down) * right) % len(i)] == '#':
                        trees = trees +1

                    index = index + 1
            else:
                i = i.rstrip()
                if i[(index * right) % len(i)] == '#':
                    trees = trees +1
                index = index + 1
        return trees
        
    print(f'1,1: {check_trees(1, 1)}')
    print(f'3,1: {check_trees(3, 1)}')
    print(f'5,1: {check_trees(5, 1)}')
    print(f'7,1: {check_trees(7, 1)}')
    print(f'1,2: {check_trees(1, 2)}')
