bags = {}
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        bag = line.split(' ', 4)
        sub_bags = {}
        for sub_bag in bag[4].split(', '):
            sub_bag_split = sub_bag.split(' ')
            if sub_bag_split[0] != 'no':
                sub_bags[sub_bag_split[1] + ' ' + sub_bag_split[2]] = int(sub_bag_split[0])
        bags[bag[0] + ' ' + bag[1]] = sub_bags

checked = []
unchecked = ['shiny gold']
while len(unchecked) > 0:
    checking_bag = unchecked[0]
    for bag in bags:
        for sub_bag in bags[bag]:
            if sub_bag == checking_bag and not bag in checked and not bag in unchecked:
                unchecked.append(bag)
    checked.append(unchecked.pop(0))

print(len(checked) - 1)
input()
