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

def get_bag_count(bag):
    count = 0
    for sub_bag in bags[bag]:
        for i in range(bags[bag][sub_bag]):
            count += 1 + get_bag_count(sub_bag)
    return count

print(get_bag_count('shiny gold'))
input()
