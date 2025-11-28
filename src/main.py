import pygame as pg
from window import display_size, display_width, display_height

pg.init()


# images section
icon_img = pg.image.load('src/img/ufo.png')
pg.display.set_icon(icon_img)

player_img = pg.image.load('src/img/player.png')
player_width = player_img.get_width()
player_height = player_img.get_height()


# starting a player
player_gap = 10
player_x = display_width // 2 - player_width // 2
player_y = display_height - player_height - player_gap


# starting a window
display = pg.display.set_mode(display_size)

# running flag
running = True


while running:
    display.blit(player_img, (player_x, player_y))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

