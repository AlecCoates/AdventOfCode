buses = []
with open("./input.txt", "r") as f:
    f.readline()
    line_split = f.readline().strip().split(',')
    for i in range(len(line_split)):
        if line_split[i] != 'x':
            buses.append((int(line_split[i]), i))

found = False
i = 1
try:
    while not found:
        found = True
        timestamp = i * buses[0][0]
        for j in range(1, len(buses)):
            if timestamp % buses[j][0] != buses[j][1]:
                found = False
                break
        i += 1
except KeyboardInterrupt:
    print(" Checked up to:", i)

print(i)
input()