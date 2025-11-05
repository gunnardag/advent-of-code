
def a(input):

    hx = 0
    hy = 0
    tailx = 0
    taily = 0
    tail_points = []

    def mv_tail(cmd, tx, ty):
        if hx != tx and hy != ty:
            if abs(hx-tx) + abs(hy-ty) > 2:
                if hx < tx:
                    tx = tx - 1
                else:
                    tx = tx + 1
                if hy < ty:
                    ty = ty - 1
                else:
                    ty = ty + 1
        elif (hx != tx or hy != ty) and abs(hx-tx) + abs(hy-ty) == 2:
            if cmd == 'U':
                tx = tx + 1
            if cmd == 'D':
                tx = tx - 1
            if cmd == 'R':
                ty = ty + 1
            if cmd == 'L':
                ty = ty - 1
        return tx, ty
                
    with open(input) as f:
        lines = f.readlines()
        for l in lines:
            cmd, val = l.split(' ')
            for i in range(0, int(val)):
                if cmd == 'U':
                    hx = hx + 1
                if cmd == 'D':
                    hx = hx - 1
                if cmd == 'R':
                    hy = hy + 1
                if cmd == 'L':
                    hy = hy - 1
                tailx, taily = mv_tail(cmd, tailx, taily)
                tail_points.append(f"{taily},{tailx}")
                #print(f"{cmd}: {taily},{tailx} -> {hy},{hx}")
    print(set(tail_points))
    return len(set(tail_points))    
print('-------------A-------------')
print(f'test: {a("testinput")}')
#print(f'real: {a("input")}')

map = ['..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................',
'..........................']

def create_map(head, tail):
    m = map.copy()
    print(head)
    hx, hy = head
    m[(hx+5)] = f"{m[hx+5][:hy+11]}H{m[hx+5][hy+12:]}"
    for t in range(0, len(tail)):
        tx, ty = tail[t]
        if m[tx+5][ty+11] == '.':
            m[(tx+5)] = f"{m[tx+5][:ty+11]}{t+1}{m[tx+5][ty+12:]}"
    for x in m[::-1]:
        print(x)
    _ = input()


def b(input):
    headx = 0
    heady = 0
    tail = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    tail_points = set()

    def mv_tail(cmd, head, ctail):
        hx, hy = head
        tx, ty = ctail
        if hx != tx and hy != ty:
            if abs(hx-tx) + abs(hy-ty) > 2:
                if hx < tx:
                    tx = tx - 1
                else:
                    tx = tx + 1
                if hy < ty:
                    ty = ty - 1
                else:
                    ty = ty + 1
        elif (hx != tx or hy != ty) and abs(hx-tx) + abs(hy-ty) == 2:
            if hx > tx:
                tx = tx + 1
            if hx < tx:
                tx = tx - 1 
            if hy > ty:
                ty = ty + 1
            if hy < ty:
                ty = ty - 1
        #print(f"{head} | {ctail} -> {(tx, ty)}")
        #create_map((headx,heady), tail)
        return (tx, ty)

    with open(input) as f:
        lines = f.readlines()
        for l in lines:
            cmd, val = l.split(' ')
            for i in range(0, int(val)):
                if cmd == 'U':
                    headx = headx + 1
                if cmd == 'D':
                    headx = headx - 1
                if cmd == 'R':
                    heady = heady + 1
                if cmd == 'L':
                    heady = heady - 1
                for x in range(0,9):
                    if x == 0:
                        tail[x] = mv_tail(cmd, (headx, heady), tail[x])
                    else:
                        tail[x] = mv_tail(cmd, tail[x-1], tail[x])
                    tail_points.add(tail[8])
    return len(tail_points)
print('-------------B-------------')
print(f'test: {b("testinput2")}')
print(f'real: {b("input")}')
