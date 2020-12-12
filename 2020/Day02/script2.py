inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        inputs.append(line)

valid = 0
for i in inputs:
    s = i.split(" ")
    n = s[0].split("-")
    c = 0
    if (s[2][int(n[0]) - 1] == s[1][0]) ^ (s[2][int(n[1]) - 1] == s[1][0]):
        valid += 1

print(valid)
input()
