from vpython import *
from time import sleep, time
from random import randint


scene = canvas(width=1500, height=800, autoscale=False)
camera_obj = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), visible=False)
scene.camera.follow(camera_obj)


def init():
    global plane_roof
    global plane_floor
    global plane_right
    global plane_left
    global planes
    global player
    global keys_pressed
    global time_text
    global s1
    global s2

    plane_roof = box(pos=vector(0, 9, 0), size=vector(
        30, 0.2, 10), color=color.gray(0.2))
    plane_floor = box(pos=vector(0, -9, 0), size=vector(30,
                      0.2, 10), color=color.gray(0.2))
    plane_right = box(pos=vector(15, 0, 0), size=vector(0.2,
                      18, 10), color=color.gray(0.3))
    plane_left = box(pos=vector(-15, 0, 0), size=vector(0.2,
                                                        18, 10), color=color.gray(0.3))
    planes = [plane_floor, plane_left, plane_right, plane_roof]
    player = box(pos=vector(0, 0, 0), size=vector(
        0.7, 1.4, 0.7), color=color.purple, acc=vector(0, 0, 0), vel=vector(0, 0, 0), make_trail=False, trail_type="curve", interval=5, retain=10, trail_color=color.orange)
    keys_pressed = wtext(pos=scene.caption_anchor)
    time_text = wtext(pos=scene.caption_anchor)
    s1 = False
    s2 = False


def stage1():
    global S1_SIZE
    S1_SIZE = 500
    for i in planes:
        i.size.z += S1_SIZE*2
    obstacles = []
    for i in range(0, int(plane_floor.size.z/2), 16):
        obstacles.append(sphere(pos=vector(0, 0, -i-8),
                         radius=2, opacity=0.1))


def stage2():
    global S2_SIZE
    S2_SIZE = 700
    for i in planes:
        i.size.z += S2_SIZE*2
    obstacles = []
    for i in range(S1_SIZE, S1_SIZE+S2_SIZE, 16):
        obstacles.append(sphere(pos=vector(0, 0, -i-8),
                         radius=3, opacity=0.1))


def pause():
    scene.waitfor('keydown')
    sleep(0.1)


def detectFloor():
    if (player.pos.y - player.size.y/2) < (plane_floor.pos.y + plane_floor.size.y/2):
        return True
    player.color = color.purple
    return False


def detectRoof():
    if (player.pos.y + player.size.y/2) > (plane_roof.pos.y - plane_roof.size.y/2):
        return True
    return False


def detectRight():
    if (player.pos.x + player.size.x/2) > (plane_right.pos.x - plane_right.size.x/2):
        return True
    return False


def detectLeft():
    if (player.pos.x - player.size.x/2) < (plane_left.pos.x + plane_left.size.x/2):
        return True
    return False


def fly():
    if detectRoof():
        player.vel.y = -0.005
        player.vel = player.vel*0.9
        player.pos.y = plane_roof.pos.y - plane_roof.size.y/2 - player.size.y/2
        return
    if detectFloor():
        player.vel.y = -0.005
        player.vel = player.vel*0.9
        player.pos.y = plane_floor.pos.y + plane_floor.size.y/2 + player.size.y/2
        return
    if detectRight():
        player.vel.x = 0
        player.vel = player.vel*0.9
        player.pos.x = plane_right.pos.x - plane_right.size.x/2 - player.size.x/2
    if detectLeft():
        player.vel.x = 0
        player.vel = player.vel*0.9
        player.pos.x = plane_left.pos.x + plane_left.size.x/2 + player.size.x/2

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


def main():
    fly()
    if s1:
        move(0.1)
    if s2:
        move(0.2)

    player.pos += player.vel
    camera_obj.pos.z = player.pos.z


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
                stage1()
                s1 = True
            if (player.pos.z < -S1_SIZE) and (not s2):
                stage2()
                s2 = True
                s1 = False
            if 'esc' in k:
                pause()
            main()

    except Exception as e:
        print(e)
