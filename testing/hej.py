from vpython import *
import os
import signal


def init():
    global scene
    global run
    scene = canvas(width=900, height=500, autoscale=False)
    run = True

    init_misc()
    init_objects()
    init_velocities()


def exit():
    global run
    run = False
    os.kill(os.getpid(), signal.SIGTERM)


def init_misc():
    global keys_pressed

    keys_pressed = wtext(pos=scene.caption_anchor)
    exit_button = button(bind=exit, text="Quit")


def init_objects():
    global paddle_1
    global paddle_2
    global ball

    ball = sphere(pos=vector(0, 0, 0), radius=1,
                  color=vector(254, 254, 254))
    paddle_1 = box(pos=vector(0, -10, 0), size=vector(5, 1, 0))
    paddle_2 = box(pos=vector(0, 10, 0), size=vector(5, 1, 0))


def init_velocities():
    paddle_1.vel = vector(0, 0, 0)
    paddle_2.vel = vector(0, 0, 0)
    ball.vel = vector(0, 0, 0)


def main():
    keys = keysdown()
    keys_pressed.text = keys

    if (paddle_1.pos.x > 15) or (paddle_1.pos.x < -15):
        paddle_1.vel.x = 0
    if (paddle_2.pos.x > 15) or (paddle_2.pos.x < -15):
        paddle_2.vel.x = 0

    if "a" in keys:
        paddle_1.vel.x = -0.2
    if "d" in keys:
        paddle_1.vel.x = 0.2
    if "left" in keys:
        paddle_2.vel.x = -0.2
    if "right" in keys:
        paddle_2.vel.x = 0.2

    paddle_1.pos += paddle_1.vel
    paddle_2.pos += paddle_2.vel


if __name__ == "__main__":
    init()
    try:
        while run:
            rate(100)
            main()

    except:
        print("ERROR")
        exit()
