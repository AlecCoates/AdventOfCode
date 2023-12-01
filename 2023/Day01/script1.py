lines = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        lines.append(line)

total_value = 0

for line in lines:
    line_value = ''
    for char in line:
        if char.isnumeric():
            line_value += char
            break
    for char in line[::-1]:
        if char.isnumeric():
            line_value += char
            break
    total_value += int(line_value)
     
print(total_value)
input()