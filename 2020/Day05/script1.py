inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        inputs.append(line.strip())

highest_id = 0
for seat in inputs:
    row = int(seat[:7].replace('F','0').replace('B','1'), 2)
    col = int(seat[7:].replace('L','0').replace('R','1'), 2)
    seat_id = row * 8 + col
    highest_id = max(highest_id, seat_id)

print(highest_id)
input()
