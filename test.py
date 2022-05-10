from vpython import *
import os
import signal
import time

scene = canvas(width=1000, height=1000, title='Reflection Shooter')


def quitgame():
    os.kill(os.getpid(), signal.SIGTERM)


'''
def Unpause():
    continue_game = True
    pause_screen.visible = False
    continue_box.visible = False'''


def pause_game():
    pause_screen.visible = True
    scene.waitfor("keydown")
    pause_screen.visible = False
    time.sleep(0.1)


quitbutton = button(text='Exit Game', bind=quitgame,
                    pos=scene.title_anchor, background=vec(1, 0, 0))
#continue_box = button(text='Continue', bind=Unpause, pos=scene.caption_anchor, background=vec(0, 1, 0))
pause_screen = text(text='Paused', pos=vec(0, 0, 0),
                    visible=False)
wall_bot = box(pos=vec(-100, 0, 0), size=vec(10, 200, 100), color=vec(0, 0, 1))
wall_mid = box(pos=vec(200, 0, 0), size=vec(10, 200, 100), color=vec(0, 0, 1))
wall_top = box(pos=vec(500, 0, 0), size=vec(10, 200, 100), color=vec(0, 0, 1))
wall_bounce = box(pos=vec(0, 300, 0), size=vec(
    200, 20, 100), color=vec(0, 0, 1))

#Terrain = [wall_bot, wall_mid, wall_top, wall_bounce]
if __name__ == "__main__":
    try:
        while True:
            rate(60)
            k = keysdown()
            if 'esc' in k:
                pause_game()
    except Exception as e:
        print(e)
