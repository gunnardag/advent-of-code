def a(input):

    data = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def check_game(game):
        result = True
        gmap = {}
        for g in game.split(', '):
            print(g)
            h = g.split(' ')
            gmap[h[1].removesuffix('\n')] = int(h[0])
        for g in gmap:
            if gmap[g] > data[g]:
                result = False
        return result
    
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            id = int(l.split(': ')[0].split(' ')[1])
            games = l.split(': ')[1].split('; ')
            r = True
            for g in games:
                if not check_game(g):
                    r = False
            if r:
                sum = sum + id
        print(sum)

#print('test:')
#a('testinput') # 8
#print('real:')
#a('input') # 2505


def b(input):

    def calculate_games(games):
        result = True
        gmap = {
            'red': 1,
            'green': 1,
            'blue': 1
        }
        for game in games:
            for g in game.split(', '):
                h = g.split(' ')
                key = h[1].removesuffix('\n')
                value = int(h[0])
                if gmap[key] < value:
                    gmap[key] = value
        sum = 1
        for g in gmap:
            sum = sum * gmap[g]
        return sum
    
    
    with open(input) as f:
        lines = f.readlines()
        sum = 0
        for l in lines:
            id = int(l.split(': ')[0].split(' ')[1])
            games = l.split(': ')[1].split('; ')
            sum = sum + calculate_games(games)
        print(sum)

print('test:')
b('testinput') # 2286
print('real:')
b('input') # 2505
