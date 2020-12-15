NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'
TURNS = [LEFT, RIGHT]
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
POS_CHANGE = {NORTH:(0,1), EAST:(1,0), SOUTH:(0,-1), WEST:(-1,0)}

actions = []
with open("./input.txt", "r") as file:
    for line in file.read().strip().split('\n'):
        actions.append((line[0], int(line[1:])))

position = (0, 0)
direction = EAST
for action in actions:
    if action[0] in TURNS:
        lr = 1
        if action[0] == LEFT:
            lr = -1
        direction = DIRECTIONS[(DIRECTIONS.index(direction) + lr * (action[1] // 90)) % 4]
    elif action[0] == FORWARD or action[0] in DIRECTIONS:
        move = direction
        if action[0] != FORWARD:
            move = action[0]
        position = (position[0] + POS_CHANGE[move][0] * action[1], position[1] + POS_CHANGE[move][1] * action[1])
        
print(abs(position[0]) + abs(position[1]))
input()