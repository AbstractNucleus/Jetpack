from vpython import *
import os
import signal


def init():
    global scene
    global run
    scene = canvas(width=900, height=500, autoscale=False)
    run = True
    misc()
    objects()
    velocities()


def exit():
    global run
    run = False
    os.kill(os.getpid(), signal.SIGTERM)


def misc():
    exit_button = button(bind=exit, text="Quit")
    

def objects():
    global keys_pressed
    global paddle_1
    global paddle_2
    global ball

    keys_pressed = wtext(pos=scene.caption_anchor)
    ball = sphere(pos=vector(0, 0, 0), radius=0.02)
    paddle_1 = box(pos=vector(0, -10, 0), axis=vector(0,0,0), size=vector(5, 1, 0))
    paddle_2 = box(pos=vector(0, 10, 0), axis=vector(0,0,0), size=vector(5, 1, 0))


def velocities():
    global paddle_1_vel
    global paddle_2_vel
    global ball_vel

    paddle_1_vel = vector(0, 0, 0)
    paddle_2_vel = vector(0, 0, 0)
    ball_vel = vector(0, 0, 0)


def main():
    keys = keysdown()
    keys_pressed.text = keys

    #print(paddle_1.pos)
    if paddle_1.pos.x == 15: paddle_1_vel.x = 0

    if "a" in keys: paddle_1_vel.x = -0.2
    if "d" in keys: paddle_1_vel.x = 0.2
    if "left" in keys: paddle_2_vel.x = -0.2
    if "right" in keys: paddle_2_vel.x = 0.2
    



    paddle_1.pos += paddle_1_vel
    paddle_2.pos += paddle_2_vel


if __name__ == "__main__":
    init()
    try:
        while run:
            rate(100)
            main()

    except:
        print("ERROR")
        exit()


    


