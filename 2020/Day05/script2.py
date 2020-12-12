inputs = []
with open("./input.txt", "r") as file:
    for line in file:
        inputs.append(line.strip())

highest_id = 0
seat_ids = []
for seat in inputs:
    row = int(seat[:7].replace('F','0').replace('B','1'), 2)
    col = int(seat[7:].replace('L','0').replace('R','1'), 2)
    seat_id = row * 8 + col
    seat_ids.append(seat_id)
    highest_id = max(highest_id, seat_id)

my_seat_id = -1
i = 0
while my_seat_id == -1:
    if i-1 in seat_ids and (not i in seat_ids) and i+1 in seat_ids:
        my_seat_id = i
        break
    i += 1

print(my_seat_id)
input()
