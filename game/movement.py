from vpython import color

def move(player, k, camera_obj, lamp):
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

    player.pos += player.vel
    moveCamera(camera_obj, lamp, player.pos)


def moveCamera(camera_obj, lamp, player_pos):
    camera_obj.pos.z = player_pos.z
    camera_obj.pos.x = player_pos.x*0.4
    lamp.pos.z = camera_obj.pos.z