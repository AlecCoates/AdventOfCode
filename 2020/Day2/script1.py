inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        inputs.append(line)

valid = 0
for i in inputs:
    s = i.split(" ")
    n = s[0].split("-")
    c = 0
    for l in s[2]:
        if l == s[1][0]:
            c += 1
    if c >= int(n[0]) and c <= int(n[1]):
        valid += 1

print(valid)
input()
