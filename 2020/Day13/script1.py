timestamp = 0
buses = []
with open("./input.txt", "r") as f:
    timestamp = int(f.readline())
    for bus in f.readline().strip().split(','):
        if bus != 'x':
            buses.append(int(bus))

next_bus = (-1, float('inf'))
for bus in buses:
    time = timestamp - timestamp % bus + bus
    if time < next_bus[1]:
        next_bus = (bus, time)

print(next_bus[0] * (next_bus[1] - timestamp))
input()