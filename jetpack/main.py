from vpython import *
from time import sleep, time
from random import randint
from settings import *


scene = canvas(width=1500, height=800, autoscale=False)
camera_obj = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), visible=False)
scene.camera.follow(camera_obj)


def init():
    global pause_text
    global plane
    global player
    global keys_pressed
    global time_text
    global s1
    global s2

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
    s1 = False
    s2 = False


def levelGen(LVL, player_pos):
    player_pos = int(player_pos)

    for i in plane.values():
        i.size.z = LENGTHS[LVL-1]
        i.pos.z = player_pos-LENGTHS[LVL-1]/2

    obstacles = []
    for i in range(-player_pos, -player_pos + LENGTHS[LVL-1], 8):
        obstacles.append(sphere(pos=vector(randint(plane["left"].pos.x+LVL, plane["right"].pos.x-LVL), randint(
            plane["down"].pos.y+LVL, plane["up"].pos.y-LVL), -i), radius=LVL, opacity=0.1, color=color.red))


def changeLevel():
    pass


def pause(pause_text):
    if not pause_text:
        pause_text = text(pos=vector(-10, 0, player.pos.z),
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


def move(v):
    player.vel.z = -v


def moveCamera(pos):
    camera_obj.pos.z = pos.z
    camera_obj.pos.x = pos.x*0.4


def main():
    detectBounds()
    fly()
    if s1:
        move(0.5)
    if s2:
        move(0.2)

    player.pos += player.vel
    moveCamera(player.pos)


if __name__ == "__main__":
    init()
    try:
        start = text(text="Press any key to start", pos=vector(0, 5, 0))
        scene.waitfor("keydown")
        start.visible = False
        t0 = time()
        t = t0

        while True:
            rate(100)

            t1 = time() - t0

            '''
                Tiden uppdaterades för ofta vilket orsakade lagg
            '''
            if int(t) < int(t1):
                time_text.text = str(int(t1))
            t = t1
            k = keysdown()
            keys_pressed.text = k
            if not s1:
                levelGen(1, player.pos.z)
                s1 = True
            if (player.pos.z < -LENGTHS[0]) and (not s2):
                levelGen(2, player.pos.z)
                s2 = True

            if 'esc' in k:
                pause(pause_text)
            main()

    except Exception as e:
        print(e)
