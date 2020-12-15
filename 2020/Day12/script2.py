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
waypoint = (10, 1)
for action in actions:
    if action[0] in TURNS:
        lr = 1
        if action[0] == LEFT:
            lr = -1
        for i in range((action[1] // 90) % 4):
            waypoint = (lr * waypoint[1], -lr * waypoint[0])
    elif action[0] in DIRECTIONS:
        waypoint = (waypoint[0] + POS_CHANGE[action[0]][0] * action[1], waypoint[1] + POS_CHANGE[action[0]][1] * action[1])
    elif action[0] == FORWARD:
        position = (position[0] + waypoint[0] * action[1], position[1] + waypoint[1] * action[1])
        
print(abs(position[0]) + abs(position[1]))
input()