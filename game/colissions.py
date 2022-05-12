from math import sqrt
from vpython import text, vector

def detectBounds(player, planes):
    # Left plane
    if (player.pos.x - player.size.x/2) < (planes["left"].pos.x + planes["left"].size.x/2):
        player.vel.x = 0
        player.vel = player.vel*0.9
        player.pos.x = planes["left"].pos.x + planes["left"].size.x/2 + player.size.x/2

    # Right plane
    if (player.pos.x + player.size.x/2) > (planes["right"].pos.x - planes["right"].size.x/2):
        player.vel.x = 0
        player.vel = player.vel*0.9
        player.pos.x = planes["right"].pos.x - planes["right"].size.x/2 - player.size.x/2

    # Top plane
    if (player.pos.y + player.size.y/2) > (planes["up"].pos.y - planes["up"].size.y/2):
        player.vel.y = -0.005
        player.vel = player.vel*0.9
        player.pos.y = planes["up"].pos.y - planes["up"].size.y/2 - player.size.y/2

    # Bottom plane
    if (player.pos.y - player.size.y/2) < (planes["down"].pos.y + planes["down"].size.y/2):
        player.vel.y = -0.005
        player.vel = player.vel*0.9
        player.pos.y = planes["down"].pos.y + planes["down"].size.y/2 + player.size.y/2

def detectColission(player, obstacles, scene):
    for obj in obstacles:
        x1, x2, y1, y2, z1, z2 = player.pos.x, obj.pos.x, player.pos.y, obj.pos.y, player.pos.z, obj.pos.z
        r1, r2 = player.radius, obj.radius

        if sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) < (r1 + r2) and obj.visible:
            end = text(pos=vector(0,5,z1), text="You Lose. \nPress r button to restart", align="center")
            scene.waitfor("keydown")
            end.visible = False
            return end