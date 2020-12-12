joltages = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        joltages.append(int(line))

joltages.append(max(joltages) + 3)
joltages.sort(reverse=True)
diff_count = [0,0,0,0]
current_joltage = 0
previous_joltage = 0
while len(joltages) > 0:
    previous_joltage = current_joltage
    current_joltage = joltages.pop()
    diff_count[current_joltage - previous_joltage] += 1

print(diff_count[1] * diff_count[3])
input()