buses = []
with open("./input.txt", "r") as f:
    f.readline()
    line_split = f.readline().strip().split(',')
    for i in range(len(line_split)):
        if line_split[i] != 'x':
            buses.append((int(line_split[i]), i, int(line_split[i]) - i))

bus_0_id = buses[0][0]
found = False
i = 0
try:
    while not found:
        i += 1
        found = True
        timestamp = i * bus_0_id
        for j in range(1, len(buses)):
            if timestamp % buses[j][0] != buses[j][2]:
                found = False
                break
except KeyboardInterrupt:
    print(" Checked up to:", i)

print(i)
print(i * buses[0][0])
input()