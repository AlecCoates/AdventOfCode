inputs = []
member_counts = []
with open("./input.txt", "r") as file:
    for group in file.read().strip().split('\n\n'):
        answers = {}
        member_count = 0
        for line in group.strip().split('\n'):
            member_count += 1
            for char in line.strip():
                if char in answers:
                    answers[char] += 1
                else:
                    answers[char] = 1
        inputs.append(answers)
        member_counts.append(member_count)

count = 0
for i in range(len(inputs)):
    for key in inputs[i]:
        if inputs[i][key] == member_counts[i]:
            count += 1

print(count)
input()
