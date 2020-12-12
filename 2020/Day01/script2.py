inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        inputs.append(int(line))

for i in inputs:
    for j in inputs:
        for k in inputs:
            if i != j and j != k and i + j + k == 2020:
                print(i * j * k)
                break
        else:
            continue
        break
    else:
        continue
    break
                
input()
