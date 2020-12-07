groups = []
with open("./input.txt", "r") as file:
    for group in file.read().strip().split('\n\n'):
        answers = []
        for line in group.split('\n'):
            for char in line.strip():
                if not char in answers:
                    answers.append(char)
        groups.append(answers)

count = 0
for group in groups:
    count += len(group)

print(count)
input()
