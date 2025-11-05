# The first column is what your opponent is going to play: 
# A for Rock, B for Paper, and C for Scissors.

# The second column, you reason, must be what you should play in response: 
# X for Rock, Y for Paper, and Z for Scissors.

def a_logic(opponent, response):
    total = 0
    if response == 'X': # I use rock
        total = total + 1
        if opponent == 'A': # vs rock
            total = total + 3
        elif opponent == 'C': # vs scissors
            total = total + 6
    elif response == 'Y': # i use paper
        total = total + 2
        if opponent == 'B': # vs paper
            total = total + 3
        elif opponent == 'A': # vs rock
            total = total + 6
    elif response == 'Z': # i use scissors
        total = total + 3
        if opponent == 'C': # vs scissors
            total = total + 3
        elif opponent == 'B': # vs paper
            total = total + 6
    else:
        print(f'response was {response} with {len(response)}')
    return total

def a(input):
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            o = l.split(' ')
            sum = sum + a_logic(o[0].strip(), o[1].strip())
        return sum
print('-------------A-------------')
print(f'test: {a("testinput")}')
print(f'real: {a("input")}')


def b_logic(opponent, response):
    total = 0
    if response == 'X': # i need to lose
        if opponent == 'A': # answer rock with scissors 
            total = total + 3
        elif opponent == 'B': # answer paper with rock
            total = total + 1
        elif opponent == 'C': # answer scissors with paper
            total = total + 2
    elif response == 'Y': # i need to draw
        if opponent == 'A': # answer rock with rock 
            total = total + 1
        elif opponent == 'B': # answer paper with paper
            total = total + 2
        elif opponent == 'C': # answer scissors with scissors
            total = total + 3
        total = total + 3
    elif response == 'Z': # i need to win
        if opponent == 'A': # answer rock with paoer 
            total = total + 2
        elif opponent == 'B': # answer paper with scissors
            total = total + 3
        elif opponent == 'C': # answer scissors with rock
            total = total + 1
        total = total + 6
    return total

def b(input):
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            o = l.split(' ')
            sum = sum + b_logic(o[0].strip(), o[1].strip())
        return sum

print('-------------B-------------')
print(f'test: {b("testinput")}')
print(f'real: {b("input")}')
