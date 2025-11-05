
def a(input):

    def check(nx, ny):
        o = ['','','','']
        t = grid[ny][nx]

        temp_y = 0
        while temp_y < ny:
            o[0] = o[0]+grid[temp_y][nx]
            temp_y = temp_y + 1

        temp_y = max_y-1
        while temp_y > ny:
            o[1] = o[1]+grid[temp_y][nx]
            temp_y = temp_y - 1
        
        temp_x = 0
        while temp_x < nx:
            o[2] = o[2]+grid[ny][temp_x]
            temp_x = temp_x + 1

        temp_x = max_x-1
        while temp_x > nx:
            o[3] = o[3]+grid[ny][temp_x]
            temp_x = temp_x - 1

        for i in o:
            k = True
            for j in i:
                if int(j) >= int(t):
                    k = False
            if k:
                return True
        return False
        

    grid = []
    x = 0
    y = 0
    visible = 0
    invisible = 0
    with open(input) as f:
        lines = f.readlines()
        for l in lines:
            grid.append(l.strip())
    max_x = len(grid[0])
    max_y = len(grid)
    while x != max_x or y != max_y:
        if x == 0 or x == max_x-1 or y == 0 or y == max_y-1:
            visible = visible + 1
        else:
            if check(x, y):
                visible =  visible + 1
            else:
                invisible = invisible + 1
        if x < max_x-1:
            x = x + 1
        elif y < max_y-1:
            x = 0
            y = y + 1
        else:
            break
    print(f"visible: {visible}")
    print(f"invisible: {invisible}")
    return visible

        

print('-------------A-------------')
print(f'test: {a("testinput")}')
print(f'real: {a("input")}')



def b(input):

    def count(nx, ny):
        o = ['','','','']
        t = int(grid[ny][nx])

        sum = 0

        temp_y = 0
        while temp_y < ny:
            o[0] = o[0]+grid[temp_y][nx]
            temp_y = temp_y + 1

        temp_y = max_y-1
        while temp_y > ny:
            o[1] = o[1]+grid[temp_y][nx]
            temp_y = temp_y - 1
        
        temp_x = 0
        while temp_x < nx:
            o[2] = o[2]+grid[ny][temp_x]
            temp_x = temp_x + 1

        temp_x = max_x-1
        while temp_x > nx:
            o[3] = o[3]+grid[ny][temp_x]
            temp_x = temp_x - 1

        o[0] = o[0][::-1]
        o[1] = o[1][::-1]
        o[2] = o[2][::-1]
        o[3] = o[3][::-1]

        print(o)
        r = []
        for p in o:
            i = 0
            for q in p:
                i = i + 1
                if int(q) >= t:
                    break
            r.append(i)
            
        print(r)
        from functools import reduce
        return reduce((lambda x, y: x * y), r)

    grid = []
    x = 0
    y = 0
    max = 0
    with open(input) as f:
        lines = f.readlines()
        for l in lines:
            grid.append(l.strip())
    max_x = len(grid[0])
    max_y = len(grid)
    while x != max_x or y != max_y:
        if x == 0 or x == max_x-1 or y == 0 or y == max_y-1:
            pass
        else:
            if count(x, y) > max:
                max = count(x, y)
        if x < max_x-1:
            x = x + 1
        elif y < max_y-1:
            x = 0
            y = y + 1
        else:
            break
    return max


print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')

"""
30373
25512
65332
33549
35390
"""