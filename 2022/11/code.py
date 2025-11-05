
def a(input):
    round = 0
    with open(input) as f:
        lines = f.readlines()


#print('-------------A-------------')
#print(f'test: {a("testinput")}')
#print(f'real: {a("input")}')


def b(input):
    with open(input) as f:
        lines = f.readlines()


print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')