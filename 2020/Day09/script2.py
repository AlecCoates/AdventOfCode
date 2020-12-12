numbers = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        numbers.append(int(line))

for i in range(25, len(numbers)):
    valid = False
    for j in range(i-25, i):
        for k in range(i-25, i):
            if numbers[j] != numbers[k] and numbers[j] + numbers[k] == numbers[i]:
                valid = True
                break
        else:
            continue
        break
    if not valid:
        break

invalid_number = numbers[i]
for i in range(len(numbers)):
    count = 0
    valid = False
    for j in range(i, len(numbers)):
        count += numbers[j]
        if count == invalid_number:
            valid = True
            break
        elif count > invalid_number:
            break
    if valid:
        break

contiguous = []
for a in range(i, j + 1):
    contiguous.append(numbers[a])

print(min(contiguous) + max(contiguous))
input()