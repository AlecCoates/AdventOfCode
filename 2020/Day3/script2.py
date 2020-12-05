inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        input_line = []
        for character in line.strip():
            input_line.append(character)
        inputs.append(input_line)

hits_multiplied = 0
for config in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    hits = 0
    right = config[0]
    down = config[1]
    for i in range(0, len(inputs), down):
        if inputs[i][((i // down) * right) % len(inputs[0])] == '#':
            hits += 1
    if hits_multiplied == 0:
        hits_multiplied = hits
    else:
        hits_multiplied *= hits

print(hits_multiplied)
input()
