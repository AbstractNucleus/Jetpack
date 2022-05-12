from random import uniform
from vpython import sphere, vector, color, text


def levelGen(LVL, player_pos, lengths, planes, sizes, obstacles):
    for i in planes.values():
        i.size.z = lengths[LVL-1]
        i.pos.z = player_pos-lengths[LVL-1]/2

    size = sizes[LVL-1]

    for i in range(int(-player_pos), int(-player_pos + lengths[LVL-1]), 8):
        obstacles.append(sphere(pos=vector(uniform(planes["left"].pos.x+size, planes["right"].pos.x-size), uniform(
            planes["down"].pos.y+size, planes["up"].pos.y-size), -i), radius=size, opacity=0.5, color=color.red))


def changeLevel(player_pos, lengths, LEVELS, planes, sizes, obstacles):
    total_length = sum(lengths[:LEVELS-1])

    global levels
    try:
        a = levels
    except:
        levels = [0 for i in range(LEVELS)]

    if not levels[0]:
        levels[0] = 1
        levelGen(1, player_pos, lengths, planes, sizes, obstacles)

    passed_length = 0
    for i, n in enumerate(levels):
        if n:
            passed_length += lengths[i]

    if total_length < -player_pos:
        end = text(pos=vector(0, 5, player_pos), text="You Won!!!")
        while True:
            j = "stop"

    for i, n in enumerate(levels):
        if (passed_length < -player_pos) and (-player_pos < passed_length+lengths[i]) and (not n):
            levels[i] = 1
            levelGen(i+1, player_pos, lengths, planes, sizes, obstacles)
            break
