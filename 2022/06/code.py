def check_marker(marker):
    for x in marker:
        if marker.count(x) > 1:
            return False
    return True

def a_logic(input):    
    a = None
    index = 0
    while a == None:
        if check_marker(input[index:index+4]):
            a = check_marker(input[index:index+4])
            print(check_marker(input[index:index+4]))
            print(index+4)
            break
        else:
            index = index + 1
def a(input):
    with open(input) as f:
        lines = f.readlines()
        for l in  lines:
            a_logic(l)

print('-------------A-------------')
print(f'test: {a("testinput")}')
print(f'real: {a("input")}')


def b_logic(input):    
    b = None
    index = 0
    while b == None:
        if check_marker(input[index:index+14]):
            b = check_marker(input[index:index+14])
            print(check_marker(input[index:index+14]))
            print(index+14)
            break
        else:
            index = index + 1
def b(input):
    with open(input) as f:
        lines = f.readlines()
        for l in  lines:
            b_logic(l)
print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')