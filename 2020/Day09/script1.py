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

print(numbers[i])
input()