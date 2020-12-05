def check_keys(passport):
    if not ('byr' in passport and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
        return False
    if not ('iyr' in passport and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
        return False
    if not ('eyr' in passport and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
        return False
    if 'hgt' in passport and len(passport['hgt']) >= 3:
        unit = passport['hgt'][-2:]
        hgt = int(passport['hgt'][:-2])
        if unit == 'cm':
            if not(hgt >= 150 and hgt <= 193):
                return False
        elif unit == 'in':
            if not(hgt >= 59 and hgt <= 76):
                return False
        else:
            return False
    else:
        return False
    if 'hcl' in passport and len(passport['hcl']) == 7 and passport['hcl'][0] == '#':
        for char in passport['hcl'][1:]:
            if not ((ord(char) >= ord('0') and ord(char) <= ord('9')) or (ord(char) >= ord('a') and ord(char) <= ord('f'))):
                return False
    else:
        return False
    if not ('ecl' in passport and passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']):
        return False
    if not ('pid' in passport and len(passport['pid']) == 9):
        return False
    return True


inputs = []
with open("./input.txt", "r") as file:
    for block in file.read().strip().split('\n\n'):
        fields = {}
        for line in block.split('\n'):
            for field in line.strip().split(' '):
                field2 = field.split(':')
                fields[field2[0]] = field2[1]
        inputs.append(fields)

count = 0
for passport in inputs:
    if check_keys(passport):
        count += 1

print(count)
input()
