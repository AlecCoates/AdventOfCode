inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        inputs.append(int(line))

for i in inputs:
    for j in inputs:
        if i != j and i + j == 2020:
            print(i * j)
            break
    else:
        continue
    break
     
input()
