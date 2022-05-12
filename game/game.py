from vpython import canvas, box, vector, local_light, color, text, keysdown, rate, sphere

from settings import *
from levels import changeLevel
from movement import move
from colissions import detectBounds, detectColission


scene = canvas(width=1500, height=800, autoscale=False)

def init():
    camera_obj = box(pos=vector(0, 0, 0), visible=False)
    scene.camera.follow(camera_obj)
    lamp = local_light(pos=camera_obj.pos, color=color.red)

    planes = {
        "up": box(pos=vector(0, 9, 0), size=vector(30, 0.2, 0), color=color.gray(0.1)),
        "down": box(pos=vector(0, -9, 0), size=vector(30, 0.2, 0), color=color.gray(0.1)),
        "left": box(pos=vector(-15, 0, 0), size=vector(0.2, 18, 0), color=color.gray(0.1)),
        "right": box(pos=vector(15, 0, 0), size=vector(0.2, 18, 0), color=color.gray(0.1))
    }

    player = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.purple, acc=vector(0, 0, 0), vel=vector(0, 0, 0), make_trail=False, trail_type="curve", interval=5, retain=10, trail_color=color.orange)

    start = text(text="Press any key to start", pos=vector(0, 5, 0))
    scene.waitfor("keydown")
    start.visible = False

    obstacles = []

    levels = [0 for i in range(LEVELS)]

    return player, camera_obj, lamp, planes, obstacles, levels, start


def pause(player_pos_z):
    pause_text = text(pos=vector(-10, 0, player_pos_z), text="Press any button to continue")
    scene.waitfor('keydown')
    pause_text.visible = False

def reset():
    player.pos = vector(0,0,0)
    camera_obj.pos = player.pos
    lamp.pos = camera_obj.pos

    planes["up"].pos = vector(0, 9, 0)
    planes["down"].pos = vector(0, -9, 0)
    planes["left"].pos = vector(-15, 0, 0)
    planes["right"].pos = vector(15, 0, 0)

    levels = [0 for i in range(LEVELS)]

    for i in obstacles:
        i.visible = False

    start.visible = True
    scene.waitfor("keydown")
    start.visible = False

    return player, camera_obj, lamp, planes, obstacles, levels, start




if __name__ == "__main__":
    player, camera_obj, lamp, planes, obstacles, levels, start = init()
    try:
        while True:
            k = keysdown()
            while True:
                rate(100)

                k = keysdown()
                if 'esc' in k:
                    pause(player.pos.z)

                detectBounds(player, planes)
                colission = detectColission(player, obstacles, scene)
                win = changeLevel(player.pos.z, lengths, LEVELS, planes, sizes, obstacles, levels, scene)

                if colission or win:
                    break

                move(player, k, camera_obj, lamp)


            if "r" in k:
                player, camera_obj, lamp, planes, obstacles, levels, start = reset()



    except Exception as e:
        raise(e)
