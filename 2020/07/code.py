def validate(data):
    # 1. BYR
    byr = int(data['byr'])
    if byr < 1920 or byr > 2002:
        print(f'byr not valid: {byr}')
        return False
    
    # 2. IYR
    iyr = int(data['iyr'])
    if iyr < 2010 or iyr > 2020:
        print(f'iyr not valid: {iyr}')
        return False
    
    # 3. EYR
    eyr = int(data['eyr'])
    if eyr < 2020 or eyr > 2030:
        print(f'eyr not valid: {eyr}')
        return False
    
    # 4. HGT
    hgt = data['hgt']
    if 'in' in hgt or 'cm' in hgt:
        hgtint = int(hgt[0:-2])
        if hgt.endswith('cm') and (hgtint < 150 or hgtint > 193):
            print(f'cm hgt not valid: {hgt}')
            return False
        if hgt.endswith('in') and (hgtint < 59 or hgtint > 76):
            print(f'in hgt not valid: {hgt}')
            return False
    else:
        print(f'hgt not valid, has no in or cm: {hgt}')
        return False

    # 5. HCL
    hcl = data['hcl']
    if not hcl.startswith('#'):
        print(f'hcl not valid: {hcl}')
        return False
    else:
        for i in hcl[1:]:
            if i not in '0123456789abcdef':
                print(f'hcl not valid: {i} not valid in {hcl}')
                return False

    # 6. ECL
    ecl = data['ecl']
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        print(f'ecl not valid: {ecl}')
        return False

    # 7. PID
    pid = data['pid']
    if len(pid) == 9:
        try:
            int(data['pid'])
        except:
            print(f'pid not valid, not only digits: {pid}')
            return False
    else:
        print(f'pid not valid, not 9 digits: {pid}')
        return False
    return True

def check_line(i):
    inputs = i.split(' ')
    if len(inputs) == 8 or (len(inputs) == 7 and 'cid:' not in i):
        a = {}
        for f in inputs:
            a[f.split(':')[0]] = f.split(':')[1]
        return validate(a)           
    return False

with open('input') as f:
    lines = f.readlines()
    valid = 0
    line = ''
    for i in lines:
        i = i.rstrip()
        if line == '':
            line = i
        else:
            line = f'{line} {i}'
        if i == '':
            if check_line(line.rstrip()):
                valid = valid + 1
            line = ''
    print(valid)
