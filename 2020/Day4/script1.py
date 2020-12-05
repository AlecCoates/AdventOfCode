def check_keys(passport):
    valid = True
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not key in passport:
            valid = False
            break
    return valid


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
