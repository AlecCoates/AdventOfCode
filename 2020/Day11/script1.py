from copy import deepcopy

FLOOR = '.'
SEAT_EMPTY = 'L'
SEAT_OCCUPIED = '#'

floor_plan = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        row = []
        for char in line.strip():
            row.append(char)
        floor_plan.append(row)

previous_floor_plan = []
while floor_plan != previous_floor_plan:
    new_floor_plan = deepcopy(floor_plan)
    for i in range(len(floor_plan)):
        for j in range(len(floor_plan[i])):
            current_space = floor_plan[i][j]
            if current_space == SEAT_EMPTY or current_space == SEAT_OCCUPIED:
                adjacent_seats = 0
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if 0 <= i+a < len(floor_plan):
                            if 0 <= j+b < len(floor_plan[i+a]):
                                if not (a == 0 and b == 0) and floor_plan[i+a][j+b] == SEAT_OCCUPIED:
                                    adjacent_seats += 1
                if current_space == SEAT_EMPTY and adjacent_seats == 0:
                    new_floor_plan[i][j] = SEAT_OCCUPIED
                elif current_space == SEAT_OCCUPIED and adjacent_seats >= 4:
                    new_floor_plan[i][j] = SEAT_EMPTY
    previous_floor_plan = deepcopy(floor_plan)
    floor_plan = deepcopy(new_floor_plan)

count = 0
for i in range(len(floor_plan)):
    for j in range(len(floor_plan[i])):
        if floor_plan[i][j] == SEAT_OCCUPIED:
            count += 1

print(count)
input()