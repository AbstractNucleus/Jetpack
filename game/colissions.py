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