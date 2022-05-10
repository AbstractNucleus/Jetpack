from vpython import *
from time import sleep, time
from random import randint
from settings import *


scene = canvas(width=1500, height=800, autoscale=False)
camera_obj = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), visible=False)
scene.camera.follow(camera_obj)
lamp = local_light(pos=camera_obj.pos, color=color.red)


def init():
    global pause_text
    global plane
    global player
    global keys_pressed
    global time_text
    global active_level
    global levels
    active_level = 0
    levels = [0, 0, 0, 0, 0]
    pause_text = False

    plane = {
        "up": box(pos=vector(0, 9, 0), size=vector(30, 0.2, 0), color=color.gray(0.1)),
        "down": box(pos=vector(0, -9, 0), size=vector(30, 0.2, 0), color=color.gray(0.1)),
        "left": box(pos=vector(-15, 0, 0), size=vector(0.2, 18, 0), color=color.gray(0.1)),
        "right": box(pos=vector(15, 0, 0), size=vector(0.2, 18, 0), color=color.gray(0.1))
    }

    player = box(pos=vector(0, 0, 0), size=vector(
        0.7, 1.4, 0.7), color=color.purple, acc=vector(0, 0, 0), vel=vector(0, 0, 0), make_trail=False, trail_type="curve", interval=5, retain=10, trail_color=color.orange)
    keys_pressed = wtext(pos=scene.caption_anchor)
    time_text = wtext(pos=scene.caption_anchor)


def levelGen(LVL, player_pos, lengths):
    for i in plane.values():
        i.size.z = lengths[LVL-1]
        i.pos.z = player_pos-lengths[LVL-1]/2

    obstacles = []
    for i in range(int(-player_pos), int(-player_pos + lengths[LVL-1]), 8):
        obstacles.append(sphere(pos=vector(randint(plane["left"].pos.x+LVL, plane["right"].pos.x-LVL), randint(
            plane["down"].pos.y+LVL, plane["up"].pos.y-LVL), -i), radius=LVL, opacity=0.5, color=color.red))


def changeLevel(player_pos, lengths):
    # active_level = 0
    # levels = [0,0,0,0,0]
    # player_pos = 0

    for i, n in enumerate(levels):
        if (lengths[i] < -player_pos < lengths[i+1]) and (not n):
            print(levels)
            levels[i] = 1
            levelGen(i+1, player_pos, lengths)
            continue


def pause(pause_text, player_pos_z):
    if not pause_text:
        pause_text = text(pos=vector(-10, 0, player_pos_z),
                          text="Press any button to continue")
    scene.waitfor('keydown')
    pause_text.visible = False


def detectBounds():
    # Left plane
    if (player.pos.x - player.size.x/2) < (plane["left"].pos.x + plane["left"].size.x/2):
        player.vel.x = 0
        player.vel = player.vel*0.9
        player.pos.x = plane["left"].pos.x + \
            plane["left"].size.x/2 + player.size.x/2

    # Right plane
    if (player.pos.x + player.size.x/2) > (plane["right"].pos.x - plane["right"].size.x/2):
        player.vel.x = 0
        player.vel = player.vel*0.9
        player.pos.x = plane["right"].pos.x - \
            plane["right"].size.x/2 - player.size.x/2

    # Top plane
    if (player.pos.y + player.size.y/2) > (plane["up"].pos.y - plane["up"].size.y/2):
        player.vel.y = -0.005
        player.vel = player.vel*0.9
        player.pos.y = plane["up"].pos.y - \
            plane["up"].size.y/2 - player.size.y/2

    # Bottom plane
    if (player.pos.y - player.size.y/2) < (plane["down"].pos.y + plane["down"].size.y/2):
        player.vel.y = -0.005
        player.vel = player.vel*0.9
        player.pos.y = plane["down"].pos.y + \
            plane["down"].size.y/2 + player.size.y/2


def fly():
    if " " in k:
        player.vel.y += 0.01
        player.color = color.orange
        player.make_trail = True
    else:
        player.vel.y -= 0.005
        player.clear_trail()
        player.make_trail = False

    if "a" in k:
        player.vel.x -= 0.005
        player.color = color.blue
    elif "d" in k:
        player.vel.x += 0.005
        player.color = color.blue
    else:
        player.vel.x = player.vel.x*0.994

    player.vel.z = -0.5


def moveCamera(pos):
    camera_obj.pos.z = pos.z
    camera_obj.pos.x = pos.x*0.4
    lamp.pos.z = camera_obj.pos.z


def main():
    changeLevel(player.pos.z, lengths)
    detectBounds()
    fly()

    player.pos += player.vel
    moveCamera(player.pos)


if __name__ == "__main__":
    init()
    try:
        start = text(text="Press any key to start", pos=vector(0, 5, 0))
        scene.waitfor("keydown")
        start.visible = False

        a = wtext(text=int(player.pos.z))
        while True:
            rate(100)

            k = keysdown()
            keys_pressed.text = k

            if 'esc' in k:
                pause(pause_text, player.pos.z)

            main()
            a.text = int(player.pos.z)

    except Exception as e:
        print(e)
