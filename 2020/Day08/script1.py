code = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        line_split = line.split(' ')
        code.append((line_split[0], int(line_split[1])))

accumulator = 0
line_no = 0
visited_lines = []
while line_no <  len(code):
    visited_lines.append(line_no)
    instruction = code[line_no][0]
    argument = code[line_no][1]
    if instruction == 'acc':
        accumulator += argument
    elif instruction == 'jmp':
        line_no += argument - 1
    elif instruction == 'nop':
        pass
    line_no += 1
    if line_no in visited_lines:
        break

print(accumulator)
input()