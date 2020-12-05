inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        input_line = []
        for character in line.strip():
            input_line.append(character)
        inputs.append(input_line)

hits = 0
slope = 3
for i in range(len(inputs)):
    if inputs[i][(i * slope) % len(inputs[0])] == '#':
        hits += 1

print(hits)
input()
