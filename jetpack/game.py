from vpython import canvas, box, vector, local_light, color, text, keysdown, rate

from settings import *
from levels import changeLevel
from movement import move, moveCamera
from colissions import detectBounds



def init():
    scene = canvas(width=1500, height=800, autoscale=False)
    camera_obj = box(pos=vector(0, 0, 0), visible=False)
    scene.camera.follow(camera_obj)
    lamp = local_light(pos=camera_obj.pos, color=color.red)

    planes = {
        "up": box(pos=vector(0, 9, 0), size=vector(30, 0.2, 0), color=color.gray(0.1)),
        "down": box(pos=vector(0, -9, 0), size=vector(30, 0.2, 0), color=color.gray(0.1)),
        "left": box(pos=vector(-15, 0, 0), size=vector(0.2, 18, 0), color=color.gray(0.1)),
        "right": box(pos=vector(15, 0, 0), size=vector(0.2, 18, 0), color=color.gray(0.1))
    }

    player = box(pos=vector(0, 0, 0), size=vector(0.7, 1.4, 0.7), color=color.purple, acc=vector(0, 0, 0), vel=vector(0, 0, 0), make_trail=False, trail_type="curve", interval=5, retain=10, trail_color=color.orange)

    start = text(text="Press any key to start", pos=vector(0, 5, 0))
    scene.waitfor("keydown")
    start.visible = False

    return scene, player, camera_obj, lamp, planes


def pause(player_pos_z):
    pause_text = text(pos=vector(-10, 0, player_pos_z), text="Press any button to continue")
    scene.waitfor('keydown')
    pause_text.visible = False


def game():
    k = keysdown()

    if 'esc' in k:
        pause(player.pos.z)

    changeLevel(player.pos.z, lengths, LEVELS, planes, sizes)

    detectBounds(player, planes)


    move(player, k, camera_obj, lamp)


if __name__ == "__main__":
    scene, player, camera_obj, lamp, planes = init()
    try:
        while True:
            rate(100)
            game()

    except Exception as e:
        print(e)
